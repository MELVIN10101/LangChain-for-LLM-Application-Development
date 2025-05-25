import requests

API_URL = "http://127.0.0.1:8000"  # Update if hosted elsewhere

def call_run_all(text):
    try:
        response = requests.post(f"{API_URL}/run-all/", json={"text": text})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("❌ Request failed:", e)
        print("💥 Raw response:", response.text if response else "No response")
        return None

def call_qa(context, question):
    try:
        response = requests.post(f"{API_URL}/qa/", json={"context": context, "question": question})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("❌ QA request failed:", e)
        print("💥 Raw response:", response.text if response else "No response")
        return None

def main():
    print("💬 Type something to analyze. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            break

        print("\n🚀 Calling /run-all/...\n")
        result = call_run_all(user_input)
        if result:
            print("📌 Summary:", result.get("summary", "N/A"))
            print("📊 Sentiment:", result.get("sentiment", "N/A"))
            print("🤖 Chat Reply:", result.get("reply", "N/A"))

        # Optional QA test
        # print("\n🧠 QA Test")
        # qa_result = call_qa(user_input, "What is the main topic?")
        # if qa_result:
        #     print("🤖 Answer:", qa_result.get("answer", "N/A"))

        print("\n" + "-"*60 + "\n")

if __name__ == "__main__":
    main()
