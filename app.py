import streamlit as st

#for multi-page apps
st.set_page_config(
    page_title="Multi-Domain Intelligence Platform",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Multi-Domain Intelligence Platform")
st.markdown("### Welcome! Please go to the sidebar to log in or register.")

st.sidebar.success("Select a page above or use navigation")