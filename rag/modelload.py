import getpass
import os
import sys
from langchain.chat_models import init_chat_model
sys.path.append(".")
from setup import setup_environment

def load_model(model_name, model_provider="openai"):
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    model = init_chat_model("gpt-4o-mini", model_provider="openai")
    if not model:
        print("Failed to load the model.")
        return None
    print("Model loaded successfully.")
    return model

if __name__ == "__main__":
    setup_environment()
    model = load_model("gpt-4o-mini", model_provider="openai")
    
    if model:
        print("Model loaded successfully.")
    else:
        print("Failed to load the model.")
    