import streamlit as st
import os

 
import platform

st.write(st.secrets["DB_USERNAME"])
st.write(st.secrets["DB_PATH"])
 

iD = "F222222" 
st.secrets["DB_USERNAME"] = iD 
st.title("Bonjour")

st.write(st.secrets["DB_USERNAME"])
