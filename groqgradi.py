#Gradio with Groq Chat Application
#pip install gradio groq

import gradio as gr
from groq import Groq

Groq_API_KEY="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"
Client=Groq(api_key=Groq_API_KEY)
def Chatbot(message,history):
    messages=[]
    for msg in history:
        messages.append(
            {"role":msg["role"],
             "content":msg["content"]
            }
        )
    messages.append(
        {"role":"user",
         "content":message
        }
    )
    response=Client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    ai_reply=response.choices[0].message.content
    history.append({"role":"user","content":message})
    history.append({"role":"assistant","content":ai_reply})
    return ai_reply
Demo=gr.ChatInterface(
    fn=Chatbot,
    title="Groq AI Chatbot",
    description="Chat with Llama3 using Groq API"
)
Demo.launch(share=True)