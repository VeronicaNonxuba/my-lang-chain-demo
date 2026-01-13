import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")   

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

llm = ChatOpenAI(model="gpt-5")
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are an agile coach. Answer any questions related to the agile process and best practices."),
    ("human", "{user_input}") 
])    

st.title("Agile guide Info")  

user_input = st.text_input("Enter your question here: ")

chain = prompt_template | llm

if user_input:
    response = chain.invoke({"user_input": user_input})
    st.write(response.content)  