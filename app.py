import streamlit as st
import os

 
import platform

st.write(st.secrets["DB_USERNAME"])
st.write(st.secrets["DB_PATH"])
 

st.write(os.environ["db_username"])

st.title("Bonjour")

