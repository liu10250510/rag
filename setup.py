import getpass
import os
import streamlit as st
def setup_environment():
    try:
        OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
        st.write(f"OPENAI_API_KEY: {OPENAI_API_KEY}")
    except ImportError:
        pass
    
if __name__ == "__main__":
    setup_environment()
    