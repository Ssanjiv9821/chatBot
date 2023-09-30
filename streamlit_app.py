
import streamlit as st
import os
"""
# Open Ai Based ChatBot

"""
os.environ['OPENAI_API_KEY'] = st.secrets["chatbot-asnnwii3pco2jv6wtzslqw"]

st.write(os.environ['OPENAI_API_KEY'])
st.write("Please type a question regarding the vision pro headet lets see if this updates!!")
st.text_input("Question", key="question")
question = st.session_state.question

print(question)