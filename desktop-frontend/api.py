import requests

API_URL = "http://127.0.0.1:8000/api"

def upload(file_path):
    with open(file_path, 'rb') as f:
        r = requests.post(f"{API_URL}/upload/", files={'file': f})
        return r.json()
