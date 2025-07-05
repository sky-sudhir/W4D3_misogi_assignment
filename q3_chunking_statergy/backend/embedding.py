import httpx
from typing import List

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
