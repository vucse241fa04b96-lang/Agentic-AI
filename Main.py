#Streamlit
#pip install streamlit
import streamlit as st
st.title("AI Agent with Groq")
st.header("Welcome to the AI Agent powered by Groq!")
st.write("This is a simple Streamlit app that demonstrates the use of Groq's AI agent capabilities.")
st.text("You can do various tasks such as generating text, executing tasks, and learning from experiences.")
st.markdown("### Example Usage:")
st.markdown("1. **Generate Text:** You can input a prompt and get a response from the AI agent.")
user_input=st.text_input("Enter your prompt:")
st.write(f"Hello, {user_input}!")
number_input=st.number_input("Enter a number to see its square:",min_value=0,max_value=1000,step=1)
if number_input:
    st.write(f"The square of {number_input} is {number_input**2}.")
user_password=st.text_input("Enter your password:",type="password")
if user_password:
    st.write("Password received. (Not displayed for security reasons)")
gender=st.radio("Select your gender:",["Male","Female","Other"])
st.write(f"You selected: {gender}")
agreement=st.checkbox("I agree to the terms and conditions.")
if agreement:
    st.write("Thank you for agreeing to the terms and conditions.")
if st.button("Submit"):
    st.write("Form submitted successfully!")