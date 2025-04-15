from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
import psycopg2

# Load model from Hugging Face
MODEL_NAME = "defog/sqlcoder-7b-2"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=150
)

# PostgreSQL connection
def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="chatbot_db",  # <-- Replace with your DB name
        user="postgres",        # <-- Replace with your DB user
        password="1234" # <-- Replace with your password
    )

# Process question → generate SQL → execute → return result
def ask_question(question):
    try:
        prompt = f"-- Convert to SQL:\n-- Question: {question}\nSELECT"
        result = generator(prompt, do_sample=False)[0]['generated_text']
        sql_query = "SELECT" + result.split("SELECT", 1)[1].split(";")[0] + ";"

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(sql_query)
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        cur.close()
        conn.close()

        formatted = [dict(zip(columns, row)) for row in rows]
        return str(formatted)

    except Exception as e:
        return f"❌ Error: {e}"