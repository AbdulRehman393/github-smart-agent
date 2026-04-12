
import streamlit as st

def report_panel(report):
    st.subheader("Analysis Report")

    st.write("## Static Analysis")
    st.json(report["static_analysis"])

    st.write("## Bug Detection")
    st.json(report["bug_detection"])

    st.write("## Optimization Suggestions")
    st.json(report["optimization"])
