import streamlit as st
 
st.set_page_config(
    page_title="Hospitals",
    page_icon="🏥",
)

st.chat_input("Please enter your question")
st.chat_button("Send")
st.chat_message("Hello! How can I help you today?")
