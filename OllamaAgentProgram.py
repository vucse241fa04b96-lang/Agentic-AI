# Ollama AI Agentic Program
# pip install ollama
# ollama run llama3.2
import ollama
Convo=[]
def Stream_ollama(prompt):
    Convo.append({'role':'user','content':prompt})
    response=""
    stream=ollama.chat(model='llama3.2',messages=Convo,stream=True)
    for chunk in stream:
        response+=chunk['message']['content']
        print(chunk['message']['content'],end='',flush=True)
    Convo.append({'role':'assisstant','content':response})
  
prompt="Explain the python OOPS?"
Stream_ollama(prompt)