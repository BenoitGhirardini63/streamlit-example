import streamlit as st
import os

 
import platform
 
my_system = platform.uname()
 
st.write(os.uname())
st.title("Bonjour")
st.write(f"System: {my_system.system}")
st.write(f"Node Name: {my_system.node}")
st.write(f"Release: {my_system.release}")
st.write(f"Version: {my_system.version}")
st.write(f"Machine: {my_system.machine}")
st.write(f"Processor: {my_system.processor}")
