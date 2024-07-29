# -*- coding: cp949 -*-
import streamlit as st

# Set the page layout to wide
st.set_page_config(layout="wide")

# Create two columns
col1, col2 = st.columns(2)

# Content for the first column
with col1:
    st.header("자료")

# Interactive chat in the second column
with col2:
    st.subheader("대화창", divider="gray")
    messages = st.container(height=400, border=True)
    if prompt := st.chat_input("질문을 입력하세요."):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")