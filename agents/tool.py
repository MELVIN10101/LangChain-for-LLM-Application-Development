from langchain.agents import Tool
from chains.sentiment import sentiment
from chains.summarizer import summarize

tools = [
    Tool(
        name="Summarize",
        func=summarize,
        description="Use this tool to summarize text. Input should be a string of text to summarize."
    ),
    Tool(
        name="Sentiment Analysis",
        func=sentiment,
        description="Use this tool to analyze the sentiment of text. Input should be a string of text to analyze."
    )
]
