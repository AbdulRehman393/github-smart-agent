<div align="center">

# 🚀 GitHub Smart Agent
### AI Agent that reads, understands, and debugs entire GitHub repositories

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-green?style=for-the-badge)](https://www.langchain.com/)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-5C2D91?style=for-the-badge)](https://github.com/facebookresearch/faiss)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge)](#)

**Turn any repository into an interactive AI assistant for code understanding, debugging, and optimization.**

</div>

---

## ✨ What is GitHub Smart Agent?

**GitHub Smart Agent** is a production-ready AI developer tool that ingests a full GitHub repository and enables you to interact with the entire codebase using natural language.

Instead of reading files one-by-one, you can ask architecture, bug, and optimization questions and get context-aware answers grounded in your code.

---

## 🔥 Core Capabilities

- 🔍 **Instant Repo Ingestion**  
  Parse and index repository structure in seconds.

- 💬 **Codebase-wide Chat**  
  Ask questions across the *entire* project, not just single files.

- 🧠 **AI + Static Bug Detection**  
  Combines deterministic checks with LLM reasoning for smarter debugging.

- ⚡ **Optimization Suggestions**  
  Performance, maintainability, and design-level recommendations with rationale.

- 📊 **Structured Analysis Reports**  
  Professional output you can share with teams/stakeholders.

---

## 🎬 Project Demo

<div align="center">

### Dashboard / Home
![Dashboard](images/dashboard.png)

### Repository Ingestion
![Repository Ingestion](images/repo_ingestion.png)

### Codebase Chat Interface
![Codebase Chat](images/codebase_chat.png)

### Bug Detection Output
![Bug Detection](images/bug_detection.png)

</div>

---

## 🧱 Architecture (High-Level)

```text
GitHub Repository
      │
      ▼
Ingestion Pipeline (tree + files + metadata)
      │
      ▼
Code Chunking + Embeddings
      │
      ▼
FAISS Vector Store (semantic retrieval)
      │
      ▼
RAG Orchestration (LangChain)
      │
      ▼
Reasoning Engine (OpenRouter: Gemini Flash / DeepSeek)
      │
      ▼
Streamlit Premium UI (chat, debugging, reports)
```

---

## 🛠️ Tech Stack

- **Backend:** Python  
- **RAG Framework:** LangChain  
- **Vector Database:** FAISS  
- **Model Gateway:** OpenRouter  
- **Models:** Gemini Flash / DeepSeek  
- **Frontend:** Streamlit (custom premium UI)

---

## 🚀 Quick Start

### 1) Clone

```bash
git clone https://github.com/AbdulRehman393/github-smart-agent.git
cd github-smart-agent
```

### 2) Create virtual environment

```bash
python -m venv .venv
```

**Windows (PowerShell)**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure environment variables

Create `.env` file from template:

```bash
cp .env.example .env
```

Add keys (example):
```env
OPENROUTER_API_KEY=your_openrouter_api_key
EMBEDDING_MODEL=your_embedding_model
LLM_MODEL=google/gemini-flash-1.5
```

### 5) Run app

```bash
streamlit run app.py
```

---

## 💡 Example Use Cases

- “Explain this repository architecture in plain English.”
- “Find likely bug hotspots in async/database layers.”
- “Which modules are tightly coupled and why?”
- “Suggest performance optimizations for this service.”
- “Generate a report for onboarding a new engineer.”

---

## 📂 Project Structure

```text
github-smart-agent/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── src/
│   ├── github_loader/
│   ├── rag/
│   ├── services/
│   └── ui/
├── images/
```

---

## 🧪 Quality & Evaluation (Recommended)

- Retrieval precision/recall tracking
- Hallucination guardrails for code-grounded responses
- Latency benchmarks (ingestion + query time)
- Prompt/version evaluation for regression control

---

## 🔐 Security Notes

- Never commit secrets (`.env`, API keys).
- Use repository privacy controls for private source code.
- Add redaction for sensitive tokens/configs during ingestion.

---

## 🗺️ Roadmap

- [ ] Multi-repo workspace support  
- [ ] PR review assistant mode  
- [ ] Architectural diagram auto-generation  
- [ ] CI integration for automated analysis on push  
- [ ] Team collaboration and report history  

---

## 🤝 Contributing

Contributions are welcome.

1. Fork this repository
2. Create a feature branch  
   `git checkout -b feature/amazing-feature`
3. Commit your changes  
   `git commit -m "feat: add amazing feature"`
4. Push and open a Pull Request

---

## 👤 Author

**Abdul Rehman**  
GitHub: [@AbdulRehman393](https://github.com/AbdulRehman393)  
LinkedIn: [khawaja-abdul-rehman-24088b266](https://www.linkedin.com/in/khawaja-abdul-rehman-24088b266)  
Email: [khawajaabdulrehman393@gmail.com](mailto:khawajaabdulrehman393@gmail.com)

---

## ⭐ Support

If this project helps you, please give it a star and share it with your network.

<div align="center">
Built for developers who need to understand unfamiliar codebases fast.
</div>
