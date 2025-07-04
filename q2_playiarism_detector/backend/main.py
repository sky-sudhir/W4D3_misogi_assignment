from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
from scipy.spatial.distance import cosine
import httpx
from fastapi.middleware.cors import CORSMiddleware
# import subprocess
# import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class TextRequest(BaseModel):
    texts: List[str]

async def get_embeddings(texts: List[str]) -> List[List[float]]:
    embeddings = []
    async with httpx.AsyncClient() as client:
        for text in texts:
            response = await client.post(
                "http://localhost:11434/api/embeddings",
                json={"model": "nomic-embed-text", "prompt": text}
            )
            response.raise_for_status()
            data = response.json()
            embeddings.append(data["embedding"])
    return embeddings

@app.post("/analyze")
async def analyze_similarity(data: TextRequest):
    texts = data.texts
    embeddings = await get_embeddings(texts)

    matrix = []
    clones = []
    for i in range(len(texts)):
        row = []
        for j in range(len(texts)):
            sim = 1 - cosine(embeddings[i], embeddings[j])
            sim_pct = round(sim * 100, 2)
            row.append(sim_pct)
            if i != j and sim_pct >= 80:
                clones.append((i, j))
        matrix.append(row)

    return {"matrix": matrix, "clones": clones}
