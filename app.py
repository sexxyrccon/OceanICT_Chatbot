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

# 소개글
with dcol1:
    st.markdown("### :red-background[더 :orange[나은] 미래, 더 :blue[푸른] 우리 바다!]")
    descr ='''<p style="color: #404040;font-size: 20px;background-color: #e6f4ff;border-radius: 5px;padding:8px;">ㅤOcean ICT는 2018년부터 2024년 현재까지 해양 관련 문제를 정보 기술을 활용하자는 취지로 진행된 부산과학고등학교의 행사입니다. 크게 해양 문화와 관광 진흥, 해양 자원의 이용 기반 구축, 해양 선박 관련 기술, 해양 생태계 및 환경 보존 4가지 분야로 나뉘어 진행됩니다. 이 행사를 통해 부산과학고등학교의 학생들은 본인이 가진 과학적, 기술적 지식을 실제 문제에 적용해보며 주변에 관심을 가지고, 사회에 기여하려는 마음가짐을 가질 수 있습니다.</p>'''
    st.html(descr)

with dcol2:
    st.image("./img/turtle.jpg")

st.divider()
st.subheader("OCEAN ICT ChatBot, :blue[한바다]:dolphin:")
st.markdown(":gray[*부산과학고에서 만든 오션ICT 챗봇 ‘한바다’로 오션 ICT 대회, 작품들에 관한 궁금증을 빠르게 해결해보세요!*]")
# 챗봇부분
col1, col2 = st.columns(2)

with col1:
    st.image("./img/samplemap.jpg")

with col2:
    st.subheader("대화창", divider="gray")
    messages = st.container(height=350, border=True)
    if prompt := st.chat_input("질문을 입력하세요."):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")