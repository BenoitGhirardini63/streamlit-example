import streamlit as st
import os

 
import platform
 
my_system = platform.uname()
 

st.title("Bonjour")
import subprocess
 
# traverse the info
Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
new = []
 
# arrange the string into clear info
for item in Id:
    new.append(str(item.split("\r")[:-1]))
for i in new:
    st.write(i[2:-2])
