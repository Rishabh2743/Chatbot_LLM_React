import anyio
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env

class GeminiProvider:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    async def get_response(self, prompt: str) -> str:
        try:
            response = await anyio.to_thread.run_sync(self.model.generate_content, prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {e}"