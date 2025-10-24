import streamlit as st

st.title("「종말 예언 : 어둠탐사기록」")


st.sidebar.title("괴담")
page = st.sidebar.radio("괴담", ["백일몽 주식 회사", "초자연 재난관리국","무명찬란교"])


if page == "백일몽 주식 회사":
    st.title("백일몽 주식 회사")

    st.write("백주사의 괴담 목록")