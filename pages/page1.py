# -*- coding:CP949 -*-

import streamlit as st

with st.sidebar:
    st.page_link("app.py", label="Home")
    st.page_link("./pages/page1.py", label="pdf")

st.title("pdf 집어넣기")