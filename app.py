import streamlit as st
import os

 
import platform
 
my_system = platform.uname()
 

st.title("Bonjour")
st.write(os.path.expanduser('~'))
