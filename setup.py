import getpass
import os
def setup_environment():
    try:
        # load environment variables from .env file (requires `python-dotenv`)
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError:
        pass
    #print("LANGSMITH_API_KEY:", os.environ.get("LANGSMITH_API_KEY"))

    os.environ["OPNAI_API_KEY"] = "true"

    if "OPNAI_API_KEY" not in os.environ:
        os.environ["OPNAI_API_KEY"] = getpass.getpass(
            prompt="Enter your OPNAI API key (optional): "
        )
    if "LANGSMITH_PROJECT" not in os.environ:
        os.environ["LANGSMITH_PROJECT"] = "Simple RAG Project"

if __name__ == "__main__":
    setup_environment()
    