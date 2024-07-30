# -*- coding:CP949 -*-

import streamlit as st

# Set the page layout to wide
st.set_page_config(layout="wide")

with st.sidebar:
    st.page_link("app.py", label="Home")
    st.page_link("./pages/page1.py", label="pdf")

# Main content
st.title("2024 7th OCEAN ICT Festival")
st.subheader(":gray[Busan Science High School]", divider = "gray")

dcol1, dcol2 = st.columns([0.7, 0.3])

# �Ұ���
with dcol1:
    st.markdown("### :red-background[�� :orange[����] �̷�, �� :blue[Ǫ��] �츮 �ٴ�!]")
    descr ='''<p style="color: #404040;font-size: 20px;background-color: #e6f4ff;border-radius: 5px;padding:8px;">��Ocean ICT�� 2018����� 2024�� ������� �ؾ� ���� ������ ���� ����� Ȱ�����ڴ� ������ ����� �λ���а���б��� ����Դϴ�. ũ�� �ؾ� ��ȭ�� ���� ����, �ؾ� �ڿ��� �̿� ��� ����, �ؾ� ���� ���� ���, �ؾ� ���°� �� ȯ�� ���� 4���� �о߷� ������ ����˴ϴ�. �� ��縦 ���� �λ���а���б��� �л����� ������ ���� ������, ����� ������ ���� ������ �����غ��� �ֺ��� ������ ������, ��ȸ�� �⿩�Ϸ��� ���������� ���� �� �ֽ��ϴ�.</p>'''
    st.html(descr)

with dcol2:
    st.image("./img/turtle.jpg")

st.divider()
st.subheader("OCEAN ICT ChatBot, :blue[�ѹٴ�]:dolphin:")
st.markdown(":gray[*�λ���а��� ���� ����ICT ê�� ���ѹٴ١��� ���� ICT ��ȸ, ��ǰ�鿡 ���� �ñ����� ������ �ذ��غ�����!*]")
# ê���κ�
col1, col2 = st.columns(2)

with col1:
    st.image("./img/samplemap.jpg")

with col2:
    st.subheader("��ȭâ", divider="gray")
    messages = st.container(height=350, border=True)
    if prompt := st.chat_input("������ �Է��ϼ���."):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")