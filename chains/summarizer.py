from transformers import pipeline

# Load summarization pipeline using a well-suited model
summarizer_pipeline = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize(text: str) -> str:
    result = summarizer_pipeline(text, max_length=130, min_length=30, do_sample=False)
    return result[0]["summary_text"]
