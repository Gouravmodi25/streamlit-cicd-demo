import streamlit as st

APP_VERSION = "v1.2"

st.set_page_config(page_title="CI/CD Demo", page_icon="🚀")

st.title("🚀 CI/CD Pipeline Demo")
st.caption(f"App version: {APP_VERSION}")

st.write("This app is deployed automatically through GitHub Actions and Render.")
st.info("v1.2: deployed automatically via GitHub Actions and Render.")

name = st.text_input("Enter your name")
if name:
    st.success(f"Hello, {name}! 👋")

number = st.slider("Pick a number", 0, 100, 25)
st.write(f"Your number squared is **{number ** 2}**")