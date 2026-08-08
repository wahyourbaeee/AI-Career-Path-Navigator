# 🧭 AI Career Path Navigator

> Platform berbasis AI yang membantu mahasiswa tech menemukan jalur karir yang tepat berdasarkan skill dan minat mereka.

![Django](https://img.shields.io/badge/Django-6.1-092E20?style=flat-square&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Gemma4-black?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

---

## 🎯 Problem

Banyak mahasiswa tech punya banyak skill tapi bingung mau spesialisasi ke mana. Pertanyaan seperti:

- *"Gua cocoknya jadi apa?"*
- *"Skill gua relevan buat karir apa?"*
- *"Harus belajar apa dulu?"*

...sering banget nggak ada jawabannya yang jelas. Platform ini hadir untuk menjawab itu.

---

## ✨ Fitur

- **Analisis Profil** — Input skill, minat, dan tujuan karir
- **Rekomendasi Spesialisasi** — AI rekomendasiin jalur karir yang paling cocok
- **Learning Path** — Daftar topik yang harus dipelajari secara berurutan
- **Skill Gap Analysis** — Tau persis skill apa yang masih kurang
- **Estimasi Timeline** — Perkiraan waktu untuk siap masuk industri

---

## 🛠️ Tech Stack

| Layer | Tech |
|---|---|
| Backend | Django 6.1 |
| AI | Ollama API (Gemma 4 31B) |
| Frontend | HTML, Tailwind CSS, Vanilla JS |
| Deployment | PythonAnywhere |

---

## 🚀 Cara Jalankan Lokal

**1. Clone repo**
```bash
git clone https://github.com/wahyourbaeee/AI-Career-Path-Navigator.git
cd AI-Career-Path-Navigator
```

**2. Buat virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**3. Setup environment variables**
```bash
cp .env.example .env
# Isi OLLAMA_API_KEY dengan key dari ollama.com
```

**4. Jalankan server**
```bash
python manage.py migrate
python manage.py runserver
```

Buka `http://localhost:8000`

---

## 🧠 Cara Kerja AI

```
User input (skills, minat, tujuan)
        ↓
Django backend format ke prompt
        ↓
Ollama API (Gemma 4 31B) proses
        ↓
Return JSON terstruktur
        ↓
Frontend render hasil visual
```

Tidak ada model yang ditraining dari scratch — project ini menggunakan **prompt engineering** untuk mengoptimalkan output dari LLM yang sudah ada.

---

## 📁 Struktur Project

```
career-path-navigator/
├── config/
│   ├── settings.py
│   └── urls.py
├── core/
│   ├── views.py       ← logic & API calls
│   ├── prompts.py     ← prompt engineering
│   └── urls.py
├── templates/
│   ├── base.html
│   └── landing.html   ← UI utama
├── .env.example
├── requirements.txt
└── manage.py
```

---

## 🔮 Roadmap

- [x] Core AI feature (analisis & rekomendasi)
- [x] Responsive landing page
- [x] Deployment
- [ ] User authentication & history
- [ ] Progress tracker per learning path
- [ ] Career comparison (A vs B)
- [ ] Integrasi job board (LinkedIn API)

---

## 👤 Author

**Wahyu Tirta**  
Internet Engineering Technology · Politeknik Negeri Lampung  
[GitHub](https://github.com/wahyourbaeee) · [LinkedIn](https://linkedin.com/in/wahyu-tirta)

---

## 📄 License

MIT License — bebas digunakan dan dimodifikasi.
