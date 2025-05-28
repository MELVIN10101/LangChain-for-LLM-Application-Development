import requests
user_id = "u1"

while True:
    text = input("You: ")
    response = requests.post("http://localhost:8000/agent", json={"user_id": user_id, "text": text})
    result = response.json()["result"]
    
    # Ensure we extract the last message from the AI only
    ai_messages = [msg for msg in result["chat_history"] if msg["type"] == "ai"]
    
    if ai_messages:
        print("Bot:", ai_messages[-1]["content"])
    else:
        print("Bot: (no AI reply found)")
