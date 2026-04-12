import streamlit as st
from src.services.ingestion_service import ingest_repository
from src.services.qa_service import build_qa_chain
from src.services.analysis_service import analyze_repository

# ----------------------------------------------------------
# Custom CSS (Professional UI)
# ----------------------------------------------------------
def apply_custom_css():
    st.markdown("""
    <style>

        /* Global background */
        .main {
            background: #F5F7FB;
        }

        /* Header gradient */
        h1 {
            background: linear-gradient(90deg, #6C63FF, #00C9A7);
            -webkit-background-clip: text;
            color: transparent;
            font-weight: 900 !important;
            letter-spacing: -1px;
        }

        /* Subheaders */
        h2, h3 {
            color: #2D2D2D !important;
            font-weight: 700;
        }

        /* Cards */
        .stCard {
            background: rgba(255, 255, 255, 0.65);
            padding: 22px;
            border-radius: 18px;
            box-shadow: 0 6px 25px rgba(0,0,0,0.08);
            backdrop-filter: blur(12px);
            margin-bottom: 22px;
        }

        /* Buttons */
        .stButton>button {
            background: linear-gradient(90deg, #6C63FF, #00C9A7);
            color: white;
            border-radius: 12px;
            border: none;
            padding: 0.70rem 1.4rem;
            font-size: 1.05rem;
            font-weight: 600;
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
            transition: all 0.2s ease;
        }
        .stButton>button:hover {
            opacity: 0.92;
            transform: scale(1.03);
        }

        /* Tabs */
        .stTabs [data-baseweb="tab"] {
            font-size: 1.15rem;
            font-weight: 600;
            padding: 12px 16px;
            border-radius: 10px;
        }
        .stTabs [data-baseweb="tab"]:hover {
            background-color: rgba(108, 99, 255, 0.15);
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #FFFFFF;
            padding: 15px;
            border-right: 1px solid #EEE;
        }

    </style>
    """, unsafe_allow_html=True)


# ----------------------------------------------------------
# Page Setup
# ----------------------------------------------------------
st.set_page_config(page_title="GitHub Smart Agent", layout="wide")
apply_custom_css()

st.title("🤖 GitHub Smart Agent")
st.caption("LangChain + FAISS + OpenRouter + Streamlit | Professional UI Edition")

# ----------------------------------------------------------
# Session State
# ----------------------------------------------------------
if "index_path" not in st.session_state:
    st.session_state.index_path = None
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None
if "repo_path" not in st.session_state:
    st.session_state.repo_path = None

# ----------------------------------------------------------
# Tabs
# ----------------------------------------------------------
tab1, tab2, tab3 = st.tabs([
    "📁 Repository",
    "💬 Chat with Codebase",
    "🧪 Analysis Report"
])

# ----------------------------------------------------------
# TAB 1 – REPOSITORY INGESTION
# ----------------------------------------------------------
with tab1:
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.header("📁 Load Repository")

    repo_url = st.text_input("GitHub Repo URL", placeholder="https://github.com/owner/repo")
    branch = st.text_input("Branch (optional)", placeholder="main")
    ingest_btn = st.button("🚀 Ingest Repository")

    if ingest_btn:
        if not repo_url.strip():
            st.error("❌ Please enter a repository URL.")
        else:
            with st.spinner("⏳ Cloning, parsing, chunking, embedding..."):
                result = ingest_repository(repo_url, branch.strip() or None)

                st.session_state.index_path = result["index_path"]
                st.session_state.repo_path = result["repo_path"]
                st.session_state.qa_chain = build_qa_chain(result["index_path"])

            st.success(f"🎉 Repository **{result['repo_name']}** ingested successfully!")
            st.info(f"📄 Files: {result['documents']} | 🧩 Chunks: {result['chunks']}")

    st.markdown('</div>', unsafe_allow_html=True)


# ----------------------------------------------------------
# TAB 2 – CHAT WITH CODEBASE
# ----------------------------------------------------------
with tab2:
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.header("💬 Chat with Codebase")

    if st.session_state.qa_chain is None:
        st.warning("⚠️ Please ingest a repository first.")
    else:
        question = st.text_area("Ask a question about the codebase:", key="chat_input")
        ask_btn = st.button("💬 Ask")

        if ask_btn:
            if not question.strip():
                st.warning("⚠️ Please enter a question.")
            else:
                with st.spinner("🤖 Thinking..."):
                    response = st.session_state.qa_chain.invoke({"query": question})

                st.subheader("📝 Answer")
                st.write(response["result"])

                st.subheader("📚 Relevant Files")
                for i, doc in enumerate(response.get("source_documents", []), start=1):
                    st.write(f"{i}. `{doc.metadata.get('path', 'unknown')}`")

    st.markdown('</div>', unsafe_allow_html=True)


# ----------------------------------------------------------
# TAB 3 – ANALYSIS REPORT
# ----------------------------------------------------------
with tab3:
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.header("🧪 Full Repository Analysis")

    if st.session_state.repo_path is None:
        st.warning("⚠️ Please ingest a repository first.")
    else:
        analyze_btn = st.button("🧪 Run Analysis Report")

        if analyze_btn:
            with st.spinner("🔍 AI is analyzing your repository..."):
                report = analyze_repository(st.session_state.repo_path)

            st.subheader("📌 Static Analysis")
            st.code(str(report["static_analysis"]), language="json")

            st.subheader("🐞 Bug Detection")
            for file, result in report["bug_detection"].items():
                st.markdown(f"### <span style='color:#6C63FF;'>{file}</span>", unsafe_allow_html=True)
                st.write(result)

            st.subheader("⚡ Optimization Suggestions")
            for file, result in report["optimization"].items():
                st.markdown(f"### <span style='color:#00C9A7;'>{file}</span>", unsafe_allow_html=True)
                st.write(result)

    st.markdown('</div>', unsafe_allow_html=True)
