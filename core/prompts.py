import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

OLLAMA_API_KEY = os.getenv('OLLAMA_API_KEY')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'gemma4:31b')

SYSTEM_PROMPT = """
Kamu adalah career advisor untuk mahasiswa tech Indonesia.
Analisis profil user dan berikan rekomendasi dalam format JSON berikut:
{
  "specialization": "nama spesialisasi",
  "reason": "alasan singkat kenapa cocok",
  "learning_path": ["topik 1", "topik 2", "topik 3"],
  "skill_gap": ["skill yang perlu dipelajari"],
  "timeline": "estimasi waktu untuk siap kerja"
}
Jawab HANYA dengan JSON valid, tanpa teks lain, tanpa markdown.
"""

def get_career_analysis(skills, interests, goal):
    response = requests.post(
        'https://api.ollama.com/api/chat',
        headers={'Authorization': f'Bearer {OLLAMA_API_KEY}'},
        json={
            "model": OLLAMA_MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Skills: {skills}\nMinat: {interests}\nTujuan: {goal}"}
            ],
            "stream": False
        }
    )
    content = response.json()['message']['content']
    return json.loads(content)