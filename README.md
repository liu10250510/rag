# RAG QA Demo

This project is a Retrieval-Augmented Generation (RAG) Question Answering system built with FastAPI, LangChain, and Streamlit. It allows users to upload a PDF, select a language model, and ask questions about the document via a web UI or API.

## Features

- Upload a PDF and ask questions about its content.
- Choose the language model and provider (default: OpenAI GPT-4o-mini).
- FastAPI backend with `/ask` endpoint.
- Streamlit user interface for easy interaction.
- Supports conversational and retrieval-based QA.

## Requirements

- Python 3.10+
- See `requirements.txt` for all dependencies.

## Installation

1. Clone the repository:
```sh
   git clone https://github.com/liu10250510/rag.git
```
2. Install dependencies:
```sh
   pip install -r requirements.txt
```
3. Set up your `.env` file with required API keys (e.g., `OPENAI_API_KEY`).

## Usage

### Start the FastAPI Backend

```sh
uvicorn ragAPI:app --reload
```

- The API will be available at `http://localhost:8000`
- Swagger UI docs: `http://localhost:8000/docs`

### Start the Streamlit UI

In a new terminal:

```sh
streamlit run rag_ui.py
```

- The UI will be available at `http://localhost:8501`

### Using the API

Send a POST request to `/ask` with:
- `file`: PDF file to upload
- `model_name`: (optional) model name, default is `gpt-4o-mini`
- `model_provider`: (optional) provider, default is `openai`
- `question`: your question

Example using `curl`:
```sh
curl -F "file=@yourfile.pdf" -F "model_name=gpt-4o-mini" -F "model_provider=openai" -F "question=What is the summary?" http://localhost:8000/ask
```

## Project Structure

```
rag/
├── ragAPI.py           # FastAPI backend
├── rag_ui.py           # Streamlit UI
├── setup.py            # Environment setup
├── requirements.txt    # Python dependencies
├── .env                # API keys and environment variables
├── rag/data/           # Uploaded and processed files (gitignored)
├── rag/docload.py      # Load document logic
├── rag/modelload.py    # Load model logic
└── rag/ragretriver.py  # RAG retrieval logic
```

## Notes

- Make sure to add your API keys to the `.env` file.
- The `rag/data/` folder is ignored by git for privacy and storage reasons.
- For production, run the backend and frontend separately.


