import asyncio

async def retry_with_backoff(func, *args, retries=3):
    for retry in range(retries):
        try:
            return await func(*args)

        except Exception as e:
            if retry == retries - 1:
                raise

            wait = 2 ** retry
            print(f"Retrying in {wait} seconds...")

            await asyncio.sleep(wait)

    return None