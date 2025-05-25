from transformers import pipeline, Conversation

chat_pipeline = pipeline("conversational", model="microsoft/DialoGPT-medium")

Conversation = {}

def chat(user_id: str, text: str)-> str:
    if user_id not in Conversation:
        Conversation[user_id] = Conversation()

    conversation = Conversation[user_id]
    conversation.add_user_input(text)
    
    response = chat_pipeline(conversation)
    bot_response = response.generated_responses[-1]
    
    return bot_response