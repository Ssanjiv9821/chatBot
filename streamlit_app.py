
import streamlit as st

"""
# Open Ai Based ChatBot

"""
st.write("Please type a question regarding the vision pro headet lets see if this updates!!")
st.text_input("Question", key="question")
question = st.session_state.question

print(question)