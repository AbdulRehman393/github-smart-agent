
import streamlit as st

def chat_panel(agent):
    st.subheader("Chat with Codebase")

    question = st.text_input("Ask a question")

    if st.button("Ask"):
        if not question.strip():
            st.warning("Please enter a question.")
            return

        with st.spinner("Thinking..."):
            response = agent.ask(question)

        st.write("### Answer")
        st.write(response["result"])
