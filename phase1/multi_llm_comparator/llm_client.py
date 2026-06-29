import httpx

from config import (
    GEMINI_API_KEY,
    GROQ_API_KEY,
    GEMINI_MODEL,
    GROQ_MODEL,
)

async def ask_gemini(prompt: str) -> str:
    """
    Send a prompt to Gemini and return the generated text.
    """
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(
            url=url,
            json=payload
        )
        response.raise_for_status()
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]

async def ask_groq(prompt: str) -> str:
    """
    Send a prompt to Groq and return the generated text.
    """
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "temperature": 0.7,
    }
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(
            url=url,
            headers=headers,
            json=payload,
        )
        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]