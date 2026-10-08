import streamlit as st

st.title("Input your information", anchor=False)
st.divider()

st.subheader("Personal Information")

name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
age = st.number_input("Age", value=None, placeholder="Enter your age")
password = st.text_input("Password", type="password")
pressed = st.button("Submit", type="primary")
st.divider()

if pressed:
    st.write("Name:", name)
    st.write("Email:", email)
    st.write("Phone Number:", phone)
    st.write("Age:", age)
    st.write("Password:", password)
