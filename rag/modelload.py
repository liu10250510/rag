import getpass
import os
import sys
sys.path.append("..")
from setup import setup_environment

def load_model(model_name, model_provider="openai"):

    try:
        if not os.environ.get("OPENAI_API_KEY"):
            os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

        from langchain.chat_models import init_chat_model

        model = init_chat_model("gpt-4o-mini", model_provider="openai")
    except Exception as e:
        print(f"Error initializing model: {e}")
        return None

    return model

if __name__ == "__main__":
    setup_environment()
    model = load_model("gpt-4o-mini", model_provider="openai")
    
    if model:
        print("Model loaded successfully.")
    else:
        print("Failed to load the model.")
    