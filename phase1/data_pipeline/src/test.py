import asyncio
import os

import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

async def main():
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        print(r.status_code)
        print(r.text)

asyncio.run(main())