import os
from dotenv import load_dotenv
from pydoc import text 
from langchain_openai import OpenAIEmbeddings
import numpy as np

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")   

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

os.getenv("OPENAI_API_KEY")

llm = OpenAIEmbeddings()

text = input("Enter your TEXT here: ")
text2 = input("Enter your TEXT here: ")
print(similarity*100,'%')