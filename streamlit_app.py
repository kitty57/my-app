import streamlit as st
from langchain.llms import OpenAI

st.title('My First Streamlit App')

user_input = st.text_input("Enter some text")
st.write('The user entered:', user_input)
