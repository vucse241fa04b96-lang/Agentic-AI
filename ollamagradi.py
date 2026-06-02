# Gradio with Ollama Chat Application
# pip install gradio ollama

import gradio as gr
import ollama

def Chatbot(message, history):

    messages = []

    # Previous chat history
    for msg in history:
        messages.append({
            "role": msg["role"],
            "content": msg["content"]
        })

    # Current user message
    messages.append({
        "role": "user",
        "content": message
    })

    # Ollama response
    response = ollama.chat(
        model="llama3",
        messages=messages
    )

    ai_reply = response["message"]["content"]

    return ai_reply


Demo = gr.ChatInterface(
    fn=Chatbot,
    title="Ollama AI Chatbot",
    description="Chat with Llama3 using Ollama"
)

Demo.launch(share=True)