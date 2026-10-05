import streamlit as st
st.title("welcome to our first website using streamlit")
name=st.text_input("What is your name ?")
if name:
  st.write("welcome !",name)
  st.balloons()
