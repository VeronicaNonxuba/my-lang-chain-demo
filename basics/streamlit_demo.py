import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.globals import set_debug

set_debug(True)
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")   

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

llm = ChatOpenAI(model="gpt-5")

st.title("Ask anything")  

question = st.text_input("Enter your question here: ")

if question:
    response = llm.invoke(question)
    st.write(response.content)  