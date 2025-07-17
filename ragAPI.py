from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import shutil
import os
import sys
sys.path.append(".")
from rag.ragretriver import ragretriver  # Adjust import if needed

app = FastAPI()

async def main():
    return """
    <html>
        <body>
            <h2>RAG QA Demo</h2>
            <form action="/ask" enctype="multipart/form-data" method="post">
                <label>Upload PDF:</label>
                <input name="file" type="file" required><br><br>
                <label>Model Name:</label>
                <input name="model_name" type="text" value="gpt-4o-mini"><br><br>
                <label>Model Provider:</label>
                <input name="model_provider" type="text" value="openai"><br><br>
                <label>Question:</label>
                <input name="question" type="text" required><br><br>
                <input type="submit">
            </form>
        </body>
    </html>
    """

@app.post("/ask")
async def ask(
    file: UploadFile = File(...),
    model_name: str = Form("gpt-4o-mini"),
    model_provider: str = Form("openai"),
    question: str = Form(...)
):
    # Save uploaded file
    os.makedirs("./rag/data/", exist_ok=True)
    file_location = f"./rag/data/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Build the retrieval chain
    qa_chain = ragretriver(file_location, model_name=model_name, model_provider=model_provider)
    if not qa_chain:
        return JSONResponse(content={"error": "Failed to initialize retrieval chain."}, status_code=500)

    # Get answer
    answer = qa_chain.invoke(question)
    return {"answer": answer}


