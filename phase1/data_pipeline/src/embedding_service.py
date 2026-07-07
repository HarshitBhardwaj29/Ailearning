import asyncio
import httpx

from config import (
    GEMINI_API_KEY,
    GEMINI_EMBEDDING_MODEL,
)


async def embed_one(text: str):
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{GEMINI_EMBEDDING_MODEL}:embedContent?key={GEMINI_API_KEY}"
    )
    
    payload = {
        "model": f"models/{GEMINI_EMBEDDING_MODEL}",
        "content": {
            "parts": [
                {
                    "text": text
                }
            ]
        }
    }

    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(url, json=payload)

        if response.status_code != 200:
            print(response.status_code)
            print(response.text)

        response.raise_for_status()

        data = response.json()

        return data["embedding"]["values"]


async def get_embeddings(batch):
    texts = batch["text"].tolist()

    tasks = [
        embed_one(text)
        for text in texts
    ]

    return await asyncio.gather(*tasks)