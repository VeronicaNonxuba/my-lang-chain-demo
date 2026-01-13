import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")   

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

print(os.getenv("OPENAI_API_KEY"))

llm = ChatOpenAI(model="gpt-5")

question = input("Enter your question here: ")
response = llm.invoke(question)
print(response.content)