import streamlit as st

st.set_page_config(
    page_title='Multiple App',
)



st.title('Main Page')

st.write('안녕하세요 "달리" 입니다 ~~뭐시기 설명')






input_user_name = st.text_input(label="User Name", value="default value")

st.sidebar.success("Select a page above")

if st.button("Confirm"):
    con = st.container()
    con.caption("Result")
    con.write(f"User Name is {str(input_user_name)}")