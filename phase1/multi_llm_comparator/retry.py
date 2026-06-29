import asyncio

async def retry_with_backoff(func, *args, retries=3):
    for attempt in range(retries):
        try:
            return await func(*args)
        except Exception as e:
            if attempt == retries - 1:
                raise e

            wait = 2 ** attempt
            await asyncio.sleep(wait)

    return None