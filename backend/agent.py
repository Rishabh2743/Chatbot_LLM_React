from llm.openai_provider import OpenAIProvider
from llm.claude_provider import ClaudeProvider
from llm.gemini_provider import GeminiProvider
import os

# Load the API key for OpenAI and others from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
claude_api_key = os.getenv("CLAUDE_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize the AI providers
providers = {
    "openai": OpenAIProvider(openai_api_key),
    "claude": ClaudeProvider(claude_api_key),
    "gemini": GeminiProvider(gemini_api_key)
}

# Select the provider based on your configuration or the request
current_provider = "openai"  # You can switch this dynamically

async def get_response(user_message: str) -> str:
    provider = providers.get(current_provider)
    if not provider:
        raise Exception(f"No provider found for {current_provider}")
    return  await provider.get_response(user_message)

