from langchain_ollama import ChatOllama 
from langchain.memory import ConversationBufferMemory

def get_llm():
    return ChatOllama(model="mistral")

user_memories= {}

def get_user_memory(user_id: str):
    print(f"Retrieving memory for user: {user_id}")
    if user_id not in user_memories:
        user_memories[user_id] = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    return user_memories[user_id]