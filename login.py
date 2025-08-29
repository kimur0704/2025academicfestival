import streamlit as st

st.set_page_config(page_title="로그인", layout="wide")

st.title("로그인")
st.write("ID와 PW를 입력하세요.")

user_id = st.text_input("ID")
user_pw = st.text_input("PW", type="password")

if st.button("로그인"):
    if user_id and user_pw:
        st.success(f"ID: {user_id}\nPW: {user_pw}")
    else:
        st.error("ID와 PW를 모두 입력하세요.")
    


