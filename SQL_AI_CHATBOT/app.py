import streamlit as st
from backend import ask_question

st.set_page_config(page_title="Chat with Your Data", layout="wide")
st.title("🧠 Chat with Your PostgreSQL Data")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ask something about your data:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        response = ask_question(user_input)
    st.session_state.messages.append({"role": "bot", "content": response})

# Display the conversation
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")
