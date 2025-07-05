# 📄 RAG Chunking Strategy Visualizer

A web application to upload PDFs and visualize different document chunking strategies for Retrieval-Augmented Generation (RAG) systems.

Built using:

* 🚀 FastAPI (backend)
* 🎈 Streamlit (frontend)
* 🧠 Local embedding API (nomic-embed-text)

---

## 🔧 Features

* ✅ Upload PDF and extract text
* 🧩 Select from multiple chunking strategies:

  * Fixed-Size
  * Recursive
  * Document-Based
  * Semantic
  * RAG Scenario (planned)
* 📊 Visualize each chunk and its metadata (size, position, etc.)
* 🧠 Semantic chunking with local embedding via `http://localhost:11434/api/embeddings`

---

## 📁 Project Structure

```
rag_chunker/
├── backend/
│   ├── main.py             # FastAPI server
│   ├── chunking.py         # Chunking strategy implementations
│   ├── utils.py            # PDF text extraction
│   └── embedding.py        # Calls local embedding model
├── frontend/
│   └── app.py              # Streamlit user interface
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rag-chunker.git
cd rag-chunker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Run the Application

### Backend (FastAPI)

```bash
uvicorn backend.main:app --reload
```

Runs at: [http://localhost:8000](http://localhost:8000)

---

### Frontend (Streamlit)

```bash
cd frontend
streamlit run app.py
```

Runs at: [http://localhost:8501](http://localhost:8501)

---

## 📦 Embedding API Setup

Make sure you have a local embedding API running:

* URL: `http://localhost:11434/api/embeddings`
* Model: `nomic-embed-text`

API POST format:

```json
{
  "model": "nomic-embed-text",
  "prompt": "Text to embed"
}
```

---

## 📌 Chunking Strategies Explained

| Strategy       | Description                                                                    |
| -------------- | ------------------------------------------------------------------------------ |
| Fixed-Size     | Splits text into fixed-length chunks (e.g., 500 chars), optionally overlapping |
| Recursive      | Recursively splits by paragraph/sentence while maintaining semantic structure  |
| Document-Based | Treats entire document or large logical units as chunks                        |
| Semantic       | Groups semantically similar sentences into coherent chunks using embeddings    |
| RAG Scenarios  | (Planned) Adaptive strategy based on RAG task type                             |

---

## 📚 Dependencies

* `fastapi`
* `uvicorn`
* `PyPDF2`
* `streamlit`
* `httpx`

---

## 📌 To Do

* [ ] Add vector visualization (e.g., using PCA/TSNE)
* [ ] Implement RAG scenario-based chunking
* [ ] Add support for uploading multiple documents
* [ ] Export chunks to JSON/CSV

---

## 🤝 Contributions

Feel free to fork this repo, improve it, and make a PR!

---

## 📜 License

MIT License

---

## 🙌 Acknowledgments

* [FastAPI](https://fastapi.tiangolo.com)
* [Streamlit](https://streamlit.io)
* [Ollama + nomic-embed-text](https://ollama.com/library/nomic-embed-text)
