import ollama
from langchain_community.llms import Ollama
ollama_llm=Ollama(
    base_url="http://localhost:11434",
    model="llama3.2"
)
response=ollama_llm.invoke("What is python oops?")
print(response)