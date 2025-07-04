# 🧠 Plagiarism Detector – Semantic Similarity Analyzer

A full-stack application for comparing semantic similarity between multiple texts using Nomic embeddings via Ollama and visualizing potential plagiarism or clone content.

---

## ✨ Features

- 🔢 Dynamic multi-text input interface (Next.js + Tailwind)
- 🧠 Semantic similarity via `nomic-embed-text` embeddings from Ollama
- 📊 Similarity matrix with pairwise percentages
- 🔍 Clone detection when similarity > 80%
- 🔁 Supports multiple embedding models (extensible)

---

## 🧩 Tech Stack

| Layer       | Tech                         |
|-------------|------------------------------|
| Frontend    | Next.js 14 (App Router), Tailwind CSS |
| Backend     | FastAPI                      |
| Embeddings  | Nomic `nomic-embed-text` via Ollama |
| Vector Math | NumPy, SciPy (cosine similarity) |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/semantic-similarity-detector.git
cd semantic-similarity-detector
