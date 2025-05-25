from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text: str) -> str:
    result = sentiment_pipeline(text)
    label = result[0]["label"]
    score = result[0]["score"]
    return f"{label} ({score:.2f})"
