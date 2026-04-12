import streamlit as st
from api_utils import send_chat_message


def render_chat(model):
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask a question about your documents..."):
        # Show user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = send_chat_message(
                        question=prompt,
                        model=model,
                        session_id=st.session_state.session_id
                    )
                    if response.status_code == 200:
                        answer = response.json().get("answer", "No response received.")
                        st.markdown(answer)
                        st.session_state.messages.append({"role": "assistant", "content": answer})
                    else:
                        st.error(f"Error: {response.text}")
                except Exception as e:
                    st.error(f"⚠️ Cannot connect to backend: {e}")