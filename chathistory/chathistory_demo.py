import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")   

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

llm = ChatOpenAI(model="gpt-5")
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are an agile coach. Answer any questions related to the agile process and best practices."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{user_input}") 
])    

chain = prompt_template | llm

history_for_chain = ChatMessageHistory(key="chat_history")

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: history_for_chain,
    input_messages_key="user_input",
    history_messages_key="chat_history"
)

print("Agile guide Info")
  
while True:
    question = input("Enter your question here: ")
    if question:
        response = chain_with_history.invoke({"user_input": question},
            config={"configurable": {"session_id": "test"}}
        )
        print(response.content)