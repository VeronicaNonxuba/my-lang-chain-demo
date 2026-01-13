import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import PromptTemplate


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")   

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

llm = ChatOpenAI(model="gpt-5")
prompt_template = PromptTemplate(
    input_variables=["city", "month", "language", "budget"], 
    template="""
    if country is fictional or non-existent, respond with "Unknown location".
        Welcome to the {city} travel guide!
        If you're visiting in {month}, here's what you can do:
        1. Must-visit attractions.
        2. Local cuisine you must try.
        3. Useful phrases in {language}.
        4. Tips for traveling on a {budget} budget.
        Enjoy your trip!    
        """
    )    

st.title("Travel guide Info")  

city = st.text_input("Enter your city here: ")
month = st.text_input("Enter your month of visit here: ")
language = st.text_input("Enter the local language here: ")
budget = st.selectbox("Enter your budget level (e.g., low, medium, high) here: ", ["low", "medium", "high"])

chain = prompt_template | llm

if month and city and language and budget:
    response = chain.invoke({"city": city, "month": month, "language": language, "budget": budget})
    st.write(response.content)  