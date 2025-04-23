# llm/openai_provider.py
import openai, os
from dotenv import load_dotenv

load_dotenv()                            # loads .env
openai.api_key = os.getenv("OPENAI_API_KEY")


import openai

class OpenAIProvider:
    def __init__(self, api_key: str):
        openai.api_key = api_key
    async def get_response(self, prompt: str) -> str:
        response = openai.completions.create(
            model="gpt-3.5-turbo",  
            prompt=prompt,
            max_tokens=150,
            temperature=0.7  # You can adjust this for more or less randomness
        )
        return response['choices'][0]['text'].strip()


