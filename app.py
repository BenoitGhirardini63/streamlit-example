import streamlit as st
import os
import wmi
 
import platform
 
my_system = platform.uname()
 

st.title("Bonjour")
st.write(f"System: {my_system.system}")
st.write(f"Node Name: {my_system.node}")
st.write(f"Release: {my_system.release}")
st.write(f"Version: {my_system.version}")
st.write(f"Machine: {my_system.machine}")
st.write(f"Processor: {my_system.processor}")


c = wmi.WMI()   
my_system = c.Win32_ComputerSystem()[0]
 
st.write(f"Manufacturer: {my_system.Manufacturer}")
st.write(f"Model: {my_system. Model}")
st.write(f"Name: {my_system.Name}")
st.write(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
st.write(f"SystemType: {my_system.SystemType}")
st.write(f"SystemFamily: {my_system.SystemFamily}")
