import streamlit as st
import os

 
import platform

st.write(st.secrets["DB_USERNAME"])
st.write(st.secrets["DB_PATH"])
 
os.environ["db_username"] == st.secrets["DB_USERNAME"]
st.write(os.environ["db_username"])

st.title("Bonjour")

