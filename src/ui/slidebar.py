
import streamlit as st

def sidebar():
    st.sidebar.header("Repository Setup")
    repo_url = st.sidebar.text_input("GitHub Repo URL")
    branch = st.sidebar.text_input("Branch (optional)")
    ingest_btn = st.sidebar.button("Ingest Repository")

    return repo_url, branch, ingest_btn
