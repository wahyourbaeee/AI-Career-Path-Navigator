import requests
import os
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    'https://api.ollama.com/api/chat',
    headers={
        'Authorization': f'Bearer {os.getenv("OLLAMA_API_KEY")}'
    },
    json={
        "model": "gemma4:31b",
        "messages": [{"role": "user", "content": "Hello, balas dengan JSON: {\"status\": \"connected\"}"}],
        "stream": False
    }
)

print(response.json())