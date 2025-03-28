import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
)

st.chat_input("Please type your message here...")
with st.chat_message("assistant"):
    st.write("Hello! How can I help you today?")
    # st.bar_chart(np.random.randn(30, 3))