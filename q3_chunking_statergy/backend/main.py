
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from utils import extract_text_from_pdf
from chunking import fixed_size_chunk, recursive_chunk, document_chunk, semantic_chunk


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...), strategy: str = "fixed", chunk_size: int = 500, overlap: int = 50):
    content = await file.read()
    text = extract_text_from_pdf(content)

    if strategy == "fixed":
        chunks = fixed_size_chunk(text, chunk_size, overlap)
    elif strategy == "recursive":
        chunks = recursive_chunk(text, chunk_size, overlap)
    elif strategy == "document":
        chunks = document_chunk(text)
    elif strategy == "semantic":
        chunks = semantic_chunk(text, chunk_size)
    else:
        return {"error": "Invalid strategy"}
    
    return {"chunks": chunks, "total_chunks": len(chunks)}
