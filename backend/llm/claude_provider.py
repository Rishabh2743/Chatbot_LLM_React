import anyio
import os
from anthropic import Anthropic, AsyncAnthropic
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env

class ClaudeProvider:
    def __init__(self):
        self.api_key = os.getenv("CLAUDE_API_KEY")
        if not self.api_key:
            raise ValueError("CLAUDE_API_KEY not found in environment variables.")

        self.client = AsyncAnthropic(api_key=self.api_key)
        self.model = "claude-3-sonnet-20240229"  # You can change to "claude-3-opus-20240229" or "claude-3-haiku-20240307"

    async def get_response(self, prompt: str) -> str:
        try:
            response = await self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                temperature=0.7,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text  # Assuming `response.content` is a list of content blocks
        except Exception as e:
            return f"Error generating response: {e}"
