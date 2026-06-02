# Streamlit and Groq Chat Application

import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="Groq AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Groq AI Chatbot Application")
st.write("Chat with Llama3 using Groq API")

# Set Groq API key
api_key = "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"

# AI Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for mesg in st.session_state.messages:
    with st.chat_message(mesg["role"]):
        st.write(mesg["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input and api_key:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Groq client
    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )

    ai_reply = response.choices[0].message.content

    # Display assistant reply
    with st.chat_message("assistant"):
        st.markdown(ai_reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )

if not api_key:
    st.warning("Please enter your Groq API key.")