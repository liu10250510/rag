from fastapi import FastAPI, File, UploadFile, Form
import tempfile
import os
from rag.ragretriver import ragretriver
import uvicorn

app = FastAPI(title="RAG API", description="Retrieval-Augmented Generation Question Answering API")

@app.post("/ask")
async def ask_question(
    file: UploadFile = File(...),
    question: str = Form(...),
    model_name: str = Form("gpt-4o-mini"),
    model_provider: str = Form("openai")
):
    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(await file.read())
        temp_file_path = temp_file.name
    
    try:
        # Create RAG retriever with the provided model and document
        qa_chain = ragretriver(temp_file_path, model_name=model_name, model_provider=model_provider)
        if not qa_chain:
            return {"error": "Failed to initialize the retrieval chain."}
        
        # Get answer
        answer = qa_chain.invoke(question)
        return {"result": answer["result"]}
    
    except Exception as e:
        return {"error": str(e)}
    
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

if __name__ == "__main__":
    uvicorn.run("ragAPI:app", host="0.0.0.0", port=8000, reload=True)
