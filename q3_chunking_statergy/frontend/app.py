# frontend/app.py
import streamlit as st
import requests

st.title("🔗 RAG Chunking Strategy Visualizer")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
strategy = st.selectbox("Select Chunking Strategy", ["fixed", "recursive", "document", "semantic"])
chunk_size = st.slider("Chunk Size", 100, 1500, 500)
overlap = st.slider("Overlap", 0, 300, 50)

if uploaded_file:
    with st.spinner("Uploading and chunking..."):
        files = {"file": uploaded_file.getvalue()}
        params = {"strategy": strategy, "chunk_size": chunk_size, "overlap": overlap}
        response = requests.post("http://localhost:8000/upload/", files=files, params=params)
        result = response.json()

        st.success(f"✅ {result['total_chunks']} Chunks Generated")
        for idx, chunk in enumerate(result["chunks"]):
            st.markdown(f"### Chunk {idx+1} ({chunk['size']} chars)")
            st.code(chunk["text"])
