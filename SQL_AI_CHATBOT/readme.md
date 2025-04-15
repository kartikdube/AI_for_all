# 🧠 Chat with Your PostgreSQL Data

An AI-powered chatbot that translates natural language into SQL, queries your PostgreSQL database, and returns results — all via a simple Streamlit web app.

---

## ✨ Features

- 💬 Ask natural questions like “What were the top selling products last month?”
- 🤖 Uses Hugging Face's `sqlcoder-7b` model to generate SQL
- 📔 Queries real-time data from your PostgreSQL database
- 🔤 Clean Streamlit UI

---

## 📁 File Structure

```
data-chatbot/
├── app.py              # Streamlit UI
├── backend.py          # Core logic (LLM + SQL execution)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. 🐍 Create & activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

### 2. 📦 Install dependencies

```bash
pip install -r requirements.txt
```

> If you encounter issues with `psycopg2`, use `psycopg2-binary` instead.

### 3. 🐘 Set up PostgreSQL

Ensure you have PostgreSQL running with the necessary tables. Example:

```sql
CREATE DATABASE chatbot_db;

-- Example tables
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT,
    price NUMERIC
);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id),
    quantity INT,
    sale_date DATE
);
```

Update your credentials in `backend.py`:

```python
conn = psycopg2.connect(
    host="localhost",
    database="chatbot_db",
    user="postgres",
    password="your_password"
)
```

### 4. 🔐 (Optional) Hugging Face API Setup

If using the hosted API instead of local model:

1. Get a token from https://huggingface.co/settings/tokens
2. Replace `API_TOKEN` in `backend.py` with your token
3. Ensure `API_URL` points to a model like `defog/sqlcoder-7b-2`

---

## 💡 Usage

```bash
streamlit run app.py
```

Then open: [http://localhost:8501](http://localhost:8501)

---

## 🧠 Model Notes

This app uses models fine-tuned for text-to-SQL translation:

- Default: [`defog/sqlcoder-7b-2`](https://huggingface.co/defog/sqlcoder-7b-2)
- Optional smaller model for CPU: `defog/sqlcoder-7b-small`

You can switch models by updating `MODEL_NAME` or `API_URL`.

---

## 📦 requirements.txt

```txt
streamlit
psycopg2-binary
transformers
torch
requests
```

---

## 📌 Troubleshooting

- **psycopg2 error?** Use `psycopg2-binary`
- **torch/streamlit crash?** Try upgrading:
  ```bash
  pip install --upgrade torch streamlit
  ```
- **Model not loading?** Use Hugging Face API with a valid token

---

## 🛠️ To-Do / Improvements

- [ ] Add SQL validation before execution
- [ ] Visualize data with charts (e.g., bar, pie)
- [ ] Store conversation history
- [ ] Add login/auth for DB security

---

## 📖 License

MIT License

