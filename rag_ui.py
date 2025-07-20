import streamlit as st
import requests
import subprocess
import time
import os
import signal
import tempfile
import sys
sys.path.append(".")
from rag.ragretriver import ragretriver

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
OPENAI_API_KEY = st.text_input("Enter your API Key", type="password")
model_name = st.text_input("Model Name", value="gpt-4o-mini")
model_provider = st.text_input("Model Provider", value="openai")
question = st.text_input("Your Question")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

if uploaded_file is not None:

    # Save the file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

if st.button("Ask") and uploaded_file and question:
    qa_chain = ragretriver(temp_file_path, model_name=model_name, model_provider=model_provider)
    if not qa_chain:
        st.error("Failed to initialize the retrieval chain.")
    else:
        # Get answer
        answer = qa_chain.invoke(question)
        st.write("Answer:", answer["result"])


