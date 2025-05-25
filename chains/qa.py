from transformers import pipeline

# Load question answering pipeline using a strong model like distilbert-base-cased
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_question(context: str, question: str) -> str:
    result = qa_pipeline(question=question, context=context)
    return result["answer"]
