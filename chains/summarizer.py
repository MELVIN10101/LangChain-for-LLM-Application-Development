from langchain.prompts import PromptTemplate
from chains.memory import get_llm
template = PromptTemplate.from_template("Summarize the following text:\n{text}\n")

def summarize(text: str):
    print(f"Summarizing text: {text}")
    llm = get_llm()
    return llm.invoke(template.format(text=text))

