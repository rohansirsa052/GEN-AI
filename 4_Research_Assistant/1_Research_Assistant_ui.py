from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt


load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant")


st.header('Reasech Assistant ')

user_input = st.text_input('Enter your Prompt')
result = model.invoke(user_input)

if st.button('Summarize'):
   st.text(result.content)
