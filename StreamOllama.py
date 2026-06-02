import streamlit as st
import ollama
st.title("🤖 Ollama AI Chatbot Application")
st.set_page_config(
    page_title="Ollama AI Chatbot",
    page_icon="🤖",
    layout="centered"
)   
if "messages" not in st.session_state:
    st.session_state.messages = []      
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
prompt = st.chat_input("Ask Anything...")
if prompt:  
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        stream=ollama.chat(
            model="llama3.2",
            messages=st.session_state.messages,
            stream=True
        )
        for chunk in stream:
            content=chunk["message"]["content"]
            full_response += content
            message_placeholder.markdown(full_response + "▌")   
        message_placeholder.markdown(full_response)
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": full_response
        }
    )