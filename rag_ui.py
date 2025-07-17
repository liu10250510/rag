import streamlit as st
import requests
import subprocess
import time
import os
import signal

# Start Uvicorn server if not already running
if "uvicorn" not in os.popen("ps aux").read():
    uvicorn_proc = subprocess.Popen(
        ["uvicorn", "ragAPI:app", "--reload"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    # Wait a bit for the server to start
    time.sleep(2)
else:
    uvicorn_proc = None

st.title("RAG QA Demo")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
model_name = st.text_input("Model Name", value="gpt-4o-mini")
model_provider = st.text_input("Model Provider", value="openai")
question = st.text_input("Your Question")

if st.button("Ask") and uploaded_file and question:
    files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
    data = {
        "model_name": model_name,
        "model_provider": model_provider,
        "question": question
    }
    response = requests.post("http://localhost:8000/ask", files=files, data=data)
    if response.ok:
        st.success(response.json()["answer"])
    else:
        st.error(response.json().get("error", "Unknown error"))



