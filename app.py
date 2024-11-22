from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemeini-flash-1.5')

def my_output(query) -> str:
    response = model.generate_content
    
#UI DEVlOPMENT using streamlit
st.set_page_config(paper_title = 'GEN AI CHATBOT')