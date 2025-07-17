from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
import sys
sys.path.append(".")
sys.path.append("..")
from rag.docload import pdf_loader
from setup import setup_environment
from rag.modelload import load_model

def ragretriver(file_path, model_name="gpt-4o-mini", model_provider="openai"):
    """
    This function sets up the environment, loads a PDF document, creates a FAISS vector store,
    and initializes a retrieval chain using a language model.
    """
    
    # Load environment variables and setup LangSmith
    setup_environment()

    docs = pdf_loader(file_path)
    
    if not docs:
        print("No documents loaded. Please check the PDF file path.")
        return None
    
    db = FAISS.from_documents(docs, OpenAIEmbeddings())
    if not db:
        print("Failed to create FAISS vector store.")
        return None
    
    retriever = db.as_retriever()
    
    if not retriever:
        print("Failed to create retriever from FAISS vector store.")
        return None
    # Load the model
    model = load_model(model_name, model_provider=model_provider)
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=model,
        retriever=retriever
    )
    
    return qa_chain

if __name__ == "__main__":
    qa_chain = ragretriver("./data/resume.pdf", model_name="gpt-4o-mini", model_provider="openai")
    
    if not qa_chain:
        print("Failed to initialize the retrieval chain.")
    else:
        print("Retrieval chain initialized successfully.")

        print(qa_chain.invoke("what is Lucy's highest level of education?"))
