import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.globals import set_debug
from langchain_core.prompts import PromptTemplate

set_debug(True)
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")   

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

llm = ChatOpenAI(model="gpt-5")
prompt_template = PromptTemplate(
    input_variables=["country"], 
    template="""
   You are an expert intraditional cuisines. You provide
    information about a specific dish from a specific country.
     
    Answer the following question: what is the traditional dish of {country}?
    """
    )    

st.title("Cuisine Info")  

country = st.text_input("Enter your country here: ")

if country:
    response = llm.invoke(prompt_template.format(country=country))
    st.write(response.content)  