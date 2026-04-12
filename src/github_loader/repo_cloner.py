import os
import shutil
import requests
import zipfile
from io import BytesIO
import urllib3


def repo_name_from_url(url: str) -> str:
    name = url.rstrip("/").split("/")[-1]
    if name.endswith(".git"):
        name = name[:-4]
    return name

def clone_repo(repo_url: str, repos_dir: str, branch: str | None = None) -> str:
    """
    Downloads the GitHub repo as a ZIP file.
    No Git installation required.
    """
    os.makedirs(repos_dir, exist_ok=True)

    repo_name = repo_name_from_url(repo_url)
    local_path = os.path.join(repos_dir, repo_name)

    # Remove existing copy
    if os.path.exists(local_path):
        shutil.rmtree(local_path)

    # Prepare GitHub ZIP URL
    if branch:
        zip_url = f"{repo_url}/archive/refs/heads/{branch}.zip"
    else:
        zip_url = f"{repo_url}/archive/refs/heads/main.zip"

    # Download ZIP
    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    response = requests.get(zip_url, verify=False)

    if response.status_code != 200:
        raise RuntimeError(f"Failed to download repository ZIP: {zip_url}")

    # Extract ZIP
    zipfile_obj = zipfile.ZipFile(BytesIO(response.content))
    zipfile_obj.extractall(repos_dir)

    # GitHub wraps contents in folder "repo_name-branch"
    extracted_name = f"{repo_name}-{branch or 'main'}"
    extracted_path = os.path.join(repos_dir, extracted_name)

    # Rename extracted folder to clean name
    os.rename(extracted_path, local_path)

    return local_path
