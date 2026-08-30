# 🎓 StudyPulse-AI

**Intelligent Learning Workspace - AI-Powered Study Material Generator**

[![Live App](https://img.shields.io/badge/Live_Demo-Streamlit-FF4B4B.svg)](https://studypulse-ai.streamlit.app/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io/)
[![Groq AI](https://img.shields.io/badge/Groq_AI-GPT_OSS_20B-f3603f.svg)](https://groq.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

🌐 **Live Demo:** [studypulse-ai.streamlit.app](https://studypulse-ai.streamlit.app/)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Overview

**StudyPulse-AI** is an ultra-fast, intelligent learning workspace that automatically generates comprehensive study materials from multiple knowledge sources. Built with **Streamlit** and powered by **Groq LPU Acceleration Engine (`openai/gpt-oss-20b`)**, it instantly transforms YouTube videos, PDF documents, and lecture notes into structured learning packets including:

- 📘 Deep concept summaries
- ⚡ Mind-blowing real-world fun facts
- 🎴 Active recall flashcards
- 📝 Exam-style PYQs with detailed solutions
- 🧩 Interactive multiple-choice quizzes

---

## ✨ Features

### 📺 Multi-Source Knowledge Extraction
- **YouTube Transcripts** - Auto-extracts transcripts directly from YouTube URLs.
- **PDF Parsing** - Extracts readable text from academic PDFs and lecture notes.
- **Direct Text Input** - Simply paste raw lecture text or custom notes.

### 🤖 AI-Powered Study Packet Generation
- **Deep Concept Summary** - In-depth breakdown covering core theories and key contexts.
- **Fun Facts** - Real-world applications and trivia derived from the content.
- **Memory Flashcards** - Expandable active-recall QA pairs.
- **Exam PYQs** - Exam-grade questions complete with detailed solution guides.
- **Interactive Quiz Engine** - Real-time multiple-choice quizzes with instant grading and explanations.

---

## 🛠️ Tech Stack

- **Frontend / UI:** [Streamlit](https://streamlit.io/)
- **LLM Engine:** [Groq Cloud LPU](https://groq.com/) (`openai/gpt-oss-20b`)
- **Document Parsing:** `pypdf`
- **Video Extraction:** `youtube-transcript-api`
- **Environment Management:** `python-dotenv`

---

## 📁 Project Structure

```text
studypulse-ai/
├── .env                  # Secret keys (local development)
├── .gitignore            # Git ignore file
├── requirements.txt      # Python dependencies
├── app.py                # Main Streamlit application
└── utils/
    ├── __init__.py
    ├── pdf_processor.py      # PDF text extractor
    ├── youtube_processor.py  # YouTube transcript handler
    └── gemini_engine.py     # Groq LLM inference integration
