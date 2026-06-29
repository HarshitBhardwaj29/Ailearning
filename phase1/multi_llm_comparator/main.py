import asyncio

from rich.console import Console
from rich.progress import Progress

from llm_client import ask_gemini, ask_groq
from retry import retry_with_backoff
from display import display_responses

console = Console()


async def main():

    prompt = "Explain Python in one sentence."

    with Progress() as progress:

        task = progress.add_task(
            "[cyan]Getting responses...",
            total=2
        )

        gemini_task = asyncio.create_task(
            retry_with_backoff(ask_gemini, prompt)
        )

        groq_task = asyncio.create_task(
            retry_with_backoff(ask_groq, prompt)
        )

        gemini = await gemini_task
        progress.advance(task)

        groq = await groq_task
        progress.advance(task)

    responses = {
        "Gemini": gemini,
        "Groq": groq,
    }

    display_responses(responses)


asyncio.run(main())