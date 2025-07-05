
import re
from typing import List, Dict

def fixed_size_chunk(text: str, chunk_size: int = 500, overlap: int = 50) -> List[Dict]:
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]
        chunks.append({"text": chunk, "start": start, "end": end, "size": len(chunk)})
        start += chunk_size - overlap
    return chunks


def recursive_chunk(text: str, chunk_size: int = 500, overlap: int = 50) -> List[Dict]:
    paragraphs = text.split("\n\n")
    chunks, current = [], ""
    for para in paragraphs:
        if len(current) + len(para) < chunk_size:
            current += para + "\n\n"
        else:
            chunks.append({"text": current.strip(), "size": len(current)})
            current = para
    if current:
        chunks.append({"text": current.strip(), "size": len(current)})
    return chunks

def document_chunk(text: str) -> List[Dict]:
    return [{"text": text.strip(), "size": len(text)}]

def semantic_chunk(text: str, chunk_size: int = 500) -> List[str]:
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks, current = [], ""
    for sentence in sentences:
        if len(current) + len(sentence) < chunk_size:
            current += sentence + " "
        else:
            chunks.append(current.strip())
            current = sentence
    if current:
        chunks.append(current.strip())
    return [{"text": chunk, "size": len(chunk)} for chunk in chunks]

# RAG scenario based can be built on top of these with config logic
