import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

st.title("💬 AI Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful assistant")
    ]

# Display previous messages
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.chat_history.append(HumanMessage(content=user_input))

    # Get response from LLM
    result = model.invoke(st.session_state.chat_history)

    response = result.content

    # Show AI message
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.chat_history.append(AIMessage(content=response))