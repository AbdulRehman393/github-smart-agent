import streamlit as st
from api_utils import upload_document, get_all_documents, delete_document


def render_sidebar():
    # Sidebar branding header
    st.sidebar.markdown("""
    <div style="
        text-align:center;
        padding: 1.5rem 0 0.9rem 0;
        background: linear-gradient(135deg,#222257 60%,#292a52 100%);
        border-radius: 0 0 20px 20px;
        box-shadow: 0 4px 24px #00000027;
    ">
        <span style="font-size:2.8rem;color:#3b82f6;">🧠</span>
        <h2 style="
          color:#89cff0;
          margin:0.7rem 0 0.1rem 0;
          font-weight:800;
          font-size:2rem;
          letter-spacing:-0.7px;
        ">DocuMind Nexus</h2>
        <p style="color:#d1d5db;font-size:0.85rem;margin:0;font-weight:600;">
           v1.0 — Intelligent RAG Assistant
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown(" ")

    # Upload section
    st.sidebar.markdown("""
    <div style="background:#181a2f;border-radius:11px;padding:1.3rem;margin-bottom:0.8rem;">
      <h4 style="color:#38bdf8;margin-bottom:0.7rem;font-weight:700;">📤 Upload Document</h4>
    """, unsafe_allow_html=True)
    uploaded_file = st.sidebar.file_uploader(
        "Select, drag or drop...", type=["pdf","docx","html"])
    upload_btn = st.sidebar.button("⬆️ Upload & Index", use_container_width=True)
    st.sidebar.markdown("</div>", unsafe_allow_html=True)
    if uploaded_file and upload_btn:
        with st.spinner("Processing document..."):
            response = upload_document(uploaded_file)
            if response.status_code == 200:
                st.sidebar.success(f"✅ Indexed: {uploaded_file.name}", icon="✅")
            else:
                st.sidebar.error(f"❌ {response.text}", icon="🚫")

    # Documents section
    st.sidebar.markdown("""
    <div style="background:#181a2f;border-radius:11px;padding:1.3rem;margin-bottom:0.8rem;">
      <h4 style="color:#a5b4fc;margin-bottom:0.7rem;font-weight:700;">📚 Documents</h4>
    """, unsafe_allow_html=True)
    documents = get_all_documents()
    if documents is None:
        st.sidebar.markdown("""
        <div style="background:#4b5563;border-radius:8px;padding:0.7rem;text-align:center;">
            <p style="color:#f85149;font-weight:700;">⚠️ Backend offline</p>
            <p style="color:#a5b4fc;font-size:0.77rem;">Run: <b>python main.py</b></p>
        </div>
        """, unsafe_allow_html=True)
    elif documents:
        for doc in documents:
            col1, col2 = st.sidebar.columns([5,1])
            col1.markdown(f"<span style='color:#dbeafe;font-weight:600;'>📄 {doc['filename']}</span>", unsafe_allow_html=True)
            if col2.button("✕", key=f"del_{doc['id']}"):
                delete_response = delete_document(doc["id"])
                if delete_response.status_code == 200:
                    st.rerun()
    else:
        st.sidebar.markdown("""
        <div style="background:#222238;border-radius:8px;padding:0.8rem;text-align:center;">
            <p style="color:#a5b4fc;font-weight:600;">No documents yet</p>
            <p style="color:#38bdf8;font-size:0.77rem;">Upload a file to get started ↑</p>
        </div>
        """, unsafe_allow_html=True)
    st.sidebar.markdown("</div>", unsafe_allow_html=True)

    # Web Search section
    st.sidebar.markdown("""
    <div style="background:#181a2f;border-radius:11px;padding:1.3rem;margin-bottom:0.8rem;">
      <h4 style="color:#38bdf8;margin-bottom:0.7rem;font-weight:700;">🔎 Web Search</h4>
      <p style="color:#a5b4fc;">Tip: Ask your web questions (such as weather, news, stocks, etc.) directly in chat!<br>
      DocuMind Nexus will automatically search the web and answer.</p>
    </div>
    """, unsafe_allow_html=True)

    # Model selection
    st.sidebar.markdown("""
    <div style="background:#181a2f;border-radius:11px;padding:1.3rem;margin-bottom:0.8rem;">
      <h4 style="color:#a5b4fc;margin-bottom:0.7rem;font-weight:700;">🤖 AI Model</h4>
    """, unsafe_allow_html=True)
    model = st.sidebar.selectbox(
        "Select model",
        [
            "nvidia/nemotron-nano-9b-v2:free",
            "qwen/qwen3-4b:free",
            "deepseek/deepseek-r1-0528:free",
            "mistralai/mistral-small-3.1-24b-instruct:free",
        ],
        index=0, label_visibility="collapsed"
    )
    st.sidebar.markdown("</div>", unsafe_allow_html=True)

    # New Conversation button
    if st.sidebar.button("🔄 New Conversation", use_container_width=True):
        import uuid
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.messages = []
        st.rerun()

    # Footer branding
    st.sidebar.markdown("""
    <div style="text-align:center;padding:1.5rem 0 0.5rem 0;">
      <span style="color:#222238;font-size:1.02rem;font-weight:700;">━━━━━━━━━━━━━━━━━</span>
      <p style="color:#dbeafe;font-size:0.82rem;margin:0.6rem 0 0 0;font-weight:500;">
        Built with <span style="color:#3b82f6;">❤️</span> by <span style="color:#38bdf8;">Abdul Rehman</span>
      </p>
      <p style="color:#a5b4fc;font-size:0.65rem;margin:0.2rem 0 0 0;">
        Powered by LangChain & OpenRouter
      </p>
    </div>
    """, unsafe_allow_html=True)

    return model