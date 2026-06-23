from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
'''
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello"
)
'''

def summarize(text):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Summarize the following text in ONE sentence.
        Keep the summary under 20 words.

        Text:
        {text}
        """
    )
    return response.text


def translate(text, language):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Translate '{text}' to {language}"
    )
    return response.text


def sentiment(text):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Analyze the sentiment of the following text.
        Rules:
        1. Return only one word.
        2. Choose from:
           Positive
           Negative
           Neutral

        Text:
        {text}
        """
    )

    return response.text.strip()