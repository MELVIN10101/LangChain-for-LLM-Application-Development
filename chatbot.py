from chains.memory import get_llm, get_user_memory

def chat(user_id,text):
    print(f"User {user_id} is chatting with the bot.")
    llm = get_llm()
    memory = get_user_memory(user_id)
    response = llm.invoke(text, memory=memory)
    return response