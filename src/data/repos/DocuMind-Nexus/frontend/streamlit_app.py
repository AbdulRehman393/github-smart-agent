import streamlit as st
import uuid
from sidebar import render_sidebar
from api_utils import send_chat_message

st.set_page_config(
    page_title="DocuMind Nexus",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
body, .stApp { background: #0a0b18 !important; }
.hero-header {
    background: linear-gradient(135deg,#222257 0,#292a52 100%);
    padding:2.4rem 0 1.6rem 0;
    text-align:center;
    border-radius:16px;
    margin-bottom:2rem;
    box-shadow: 0 6px 24px rgba(0,0,0,0.30);
}
.hero-header h1 {
    color:#fff;font-weight:900;font-size:3.2rem;letter-spacing:-1px;margin:0;
}
.hero-header p {color:#dbeafe;font-size:1.2rem;font-weight:500;margin-top:0.2rem;}
.info-bar {display:flex;justify-content:center;gap:2rem;padding:0.8rem 0;margin-bottom:1.2rem;}
.info-item {
    background:#181a2f;border-radius:14px;padding:0.5rem 1.3rem;
    color:#3b82f6;font-weight:700;font-size:1rem;display:flex;align-items:center;gap:0.6rem;
    box-shadow:0 2px 8px rgba(59,130,246,0.07);
}
.stButton > button {
    background: linear-gradient(90deg,#3B82F6 0%,#8B5CF6 100%) !important;
    color:#fff !important;font-weight:700 !important;
    border-radius:11px !important;font-size:1.14rem!important;box-shadow:0 2px 12px #6366f126;
}
[data-testid="stSidebar"]{background:#181a2f!important;}
[data-testid="stSidebar"] h2,[data-testid="stSidebar"] p,[data-testid="stSidebar"] span{color:#38bdf8!important;}
.stFileUploaderDragDrop {background:rgba(59,130,246,0.1)!important;}
[data-testid="stChatMessage"]{
    background:#222238!important;margin-bottom:0.9rem!important;
    border:1px solid #31316b!important;border-radius:16px!important;
    padding:1.4rem!important;box-shadow:0 2px 12px #6366f126;
}
[data-testid="stChatMessage"] p,[data-testid="stChatMessage"] li,[data-testid="stChatMessage"] span{
    color:#dbeafe!important;font-size:1.06rem!important;
}
.welcome-card {
    background:#181a2f;border-radius:16px;
    padding:2.7rem 2rem;text-align:center;margin-bottom:2.2rem;
    box-shadow:0 12px 36px #0009;
}
.welcome-card h3 {color:#3b82f6;font-size:1.3rem;font-weight:700;margin-bottom:1rem;}
.welcome-card p {color:#dbeafe;font-size:1.04rem;}
.feature-grid {display:flex;justify-content:center;gap:1.2rem;margin-top:1.7rem;}
.feature-item {
    background:rgba(59,130,246,0.13);border:1px solid #3b82f6;
    border-radius:13px;padding:1rem 1.3rem;width:170px;text-align:center;
    box-shadow:0 2px 10px #6366f130;
}
.feature-item .icon {font-size:1.7rem;margin-bottom:0.35rem;color:#3b82f6;}
.feature-item .label {color:#dbeafe;font-size:0.95rem;font-weight:700;}
::-webkit-scrollbar{width:7px;}
::-webkit-scrollbar-thumb{background:#232b4d;border-radius:5px;}
</style>
""", unsafe_allow_html=True)

# Session state
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "messages" not in st.session_state:
    st.session_state.messages = []

model = render_sidebar()

# Header
st.markdown("""
<div class="hero-header">
    <h1>🧠 DocuMind Nexus</h1>
    <p>Upload your docs. Ask anything. Get smart answers.</p>
</div>
""", unsafe_allow_html=True)

# Info bar
model_short = model.split('/')[1].split(':')[0] if '/' in model else model
st.markdown(f"""
<div class="info-bar">
    <span class="info-item">🟢 Online</span>
    <span class="info-item">Model: {model_short}</span>
    <span class="info-item">Session: {st.session_state.session_id[:8]}</span>
</div>
""", unsafe_allow_html=True)

# Welcome card (empty chat)
if not st.session_state.messages:
    st.markdown("""
    <div class="welcome-card">
        <h3>👋 Welcome to DocuMind Nexus — Your Document Chat Assistant</h3>
        <p>Upload PDF, DOCX, or HTML files via the sidebar. Then ask anything!</p>
        <div class="feature-grid">
            <div class="feature-item">
                <div class="icon">📄</div>
                <div class="label">Upload Documents</div>
            </div>
            <div class="feature-item">
                <div class="icon">💬</div>
                <div class="label">Chat with AI</div>
            </div>
            <div class="feature-item">
                <div class="icon">⚡</div>
                <div class="label">Quick, Relevant Answers</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

for msg in st.session_state.messages:
    avatar = "🧑‍💻" if msg["role"] == "user" else "🧠"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask anything about your documents..."):
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant", avatar="🧠"):
        with st.spinner("🧠 Thinking..."):
            try:
                response = send_chat_message(prompt, model, st.session_state.session_id)
                if response.status_code == 200:
                    payload = response.json()

                    returned_session_id = payload.get("session_id")
                    if returned_session_id:
                        st.session_state.session_id = returned_session_id

                    answer = payload.get("answer", "")
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error(f"❌ Error: {response.text}")
            except Exception as e:
                st.error(f"❌ {str(e)}")