# -*- coding: cp949 -*-
import streamlit as st

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for content in st.session_state.chat_history:
    with st.chat_message(content["role"]):
        st.markdown(content['message'])    

if prompt := st.chat_input("�޽����� �Է��ϼ���."):
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.chat_history.append({"role": "user", "message": prompt})

    with st.chat_message("ai"):                
        response = f'{prompt}... {prompt}... {prompt}...'
        st.markdown(response)
        st.session_state.chat_history.append({"role": "ai", "message": response})
