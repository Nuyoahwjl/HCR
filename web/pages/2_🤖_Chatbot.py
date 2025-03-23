import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
)

st.chat_input("assistant")
with st.chat_message("Hello! How can I help you today?"):
    st.write("Hello! How can I help you today?")
    st.bar_chart(np.random.randn(30, 3))