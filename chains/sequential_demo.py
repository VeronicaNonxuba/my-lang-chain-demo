import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")   

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

llm = ChatOpenAI(model="gpt-5")
title_prompt = PromptTemplate(
    input_variables=["topic"], 
    template="""
            You are an experienced speech writer.
            You need to craft an impactful title for a speech 
            on the following topic: {topic}
            Answer exactly with one title.  
        """
    )    

speech_prompt = PromptTemplate(
    input_variables=["title"], 
    template="""
            You need to write a powerful {emotion} speech of 150 words
            for the following title: {title}.
            Format the output with 2 keys: 'title' and 'speech'. and fill 
            them with the title and the speech respectively.
        """
    )    

first_chain = title_prompt | llm | StrOutputParser() | (lambda title: (st.write(title), title)[1])
second_chain = speech_prompt | llm | JsonOutputParser()
chain = first_chain | (lambda title: {"title": title, "emotion": emotion}) | second_chain

st.title("Speech Generator")  

topic = st.text_input("Enter the topic: ")
emotion= st.text_input("Enter the emotion of the speech (e.g., inspiring, humorous, serious): ")

if topic and emotion:
    response = chain.invoke({"topic": topic})
    st.write(response)  
    st.write(response["title"]) 