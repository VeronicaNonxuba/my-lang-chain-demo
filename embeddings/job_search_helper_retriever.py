import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")   

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

os.getenv("OPENAI_API_KEY")

llm = OpenAIEmbeddings()

document = TextLoader("./embeddings/job_listings.txt").load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=10)
chunks = text_splitter.split_documents(document)
vector_store = Chroma.from_documents(chunks, llm)
retriever = vector_store.as_retriever()

text = input("Enter your query here: ")

docs = retriever.invoke(text)

for doc in docs:
    print(doc.page_content)