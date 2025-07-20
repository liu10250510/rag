import getpass
import os
import streamlit as st
from dotenv import load_dotenv

def setup_environment():
    """
    Set up the environment by loading the OpenAI API key from various sources.
    Priority order:
    1. Predefined environment variables
    2. .env file
    3. Streamlit secrets (when running in Streamlit)
    
    Returns:
        str: The OpenAI API key
    """
    # Initialize API key variable
    api_key = None
    source = None
    
    # Case 1: Check predefined environment variables first
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        source = "predefined environment variables"
    
    # Case 2: If not found, try loading from .env file
    if not api_key:
        # Don't override existing environment variables
        load_dotenv(override=False)
        # Check if the .env file provided a key
        api_key = os.environ.get("OPENAI_API_KEY")
        if api_key:
            source = ".env file"
    
    # Case 3: If still not found, try Streamlit secrets
    if not api_key:
        try:
            api_key = st.secrets["OPENAI_API_KEY"]
            if api_key:
                os.environ["OPENAI_API_KEY"] = api_key
                source = "Streamlit secrets"
        except:
            pass
    
    # Log the source of the API key (if found)
    if api_key:
        print(f"API key loaded from {source}")
    else:
        print("Warning: No API key found")
        
    return api_key
    
if __name__ == "__main__":
    setup_environment()