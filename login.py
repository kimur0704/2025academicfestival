import streamlit as st

st.set_page_config(
    page_title="로그인",
    page_icon="🔒",
    layout="centered"
)

st.title("🔒 로그인")
st.markdown("학번과 비밀번호를 입력하세요.")

student_id = st.text_input("학번", placeholder="학번을 입력하세요")
password = st.text_input("비밀번호", type="password", placeholder="비밀번호를 입력하세요")

if st.button("로그인"):
    if student_id and password:
        st.success(f"학번: {student_id}\n비밀번호: {password}")
        # 실제 로그인 처리 로직은 여기에 추가
    else:
        st.error("학번과 비밀번호를 모두 입력하세요.")
        


