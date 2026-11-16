import streamlit as st

# Title
st.title("Simple Streamlit App")

# Subtitle
st.write("Welcome to my first Streamlit application!")

# User Input
name = st.text_input("Enter your name")

# Display Output
if name:
    st.write("Hello,", name)
    st.success("Welcome to Streamlit!")
