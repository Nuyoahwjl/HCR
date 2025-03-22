import streamlit as st
 
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
)

st.chat_input("Please enter your question")
st.chat_message("Hello! How can I help you today?")
