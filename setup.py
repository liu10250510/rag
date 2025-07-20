import getpass
import os
import streamlit as st

def setup_environment():
    # Try to get API key from Streamlit secrets
    try:
        api_key = st.secrets["OPENAI_API_KEY"]
        os.environ["OPENAI_API_KEY"] = api_key
    except:
        # If not in Streamlit secrets, check environment variables
        api_key = os.environ.get("OPENAI_API_KEY")
        
    return api_key
    
if __name__ == "__main__":
    setup_environment()