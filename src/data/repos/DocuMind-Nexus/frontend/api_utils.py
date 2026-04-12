import requests

API_URL = "http://127.0.0.1:8000"
# For deployment, set for example:
# API_URL = "https://your-backend-url.onrender.com"

def upload_document(file):
    files = {"file": (file.name, file.getvalue())}
    response = requests.post(f"{API_URL}/upload-doc", files=files, timeout=120)
    return response

def get_all_documents():
    try:
        response = requests.get(f"{API_URL}/list-docs", timeout=10)
        if response.status_code == 200:
            return response.json()
        return []
    except requests.exceptions.ConnectionError:
        return None

def delete_document(file_id):
    response = requests.post(f"{API_URL}/delete-doc", json={"file_id": file_id}, timeout=30)
    return response

def send_chat_message(question, model, session_id):
    response = requests.post(
        f"{API_URL}/chat",
        json={
            "question": question,
            "model": model,
            "session_id": session_id
        },
        timeout=120
    )
    return response