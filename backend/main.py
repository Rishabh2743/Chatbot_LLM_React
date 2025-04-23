from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llm.gemini_provider import GeminiProvider  # Corrected import (case-sensitive)
from llm.openai_provider import OpenAIProvider
from llm.claude_provider import ClaudeProvider
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize FastAPI app
app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class MessageRequest(BaseModel):
    message: str
    model: str  # 'gpt' or 'gemini'

# Response schema
class MessageResponse(BaseModel):
    response: str

api_key = os.getenv("OPENAI_API_KEY")
# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Chatbot API!"}
   
# POST endpoint to send message to LLM
@app.post("/send_message", response_model=MessageResponse)
async def send_message(req: MessageRequest):  # <-- Make this async
    try:
        if req.model == "gpt":
            ai_provider = OpenAIProvider(api_key)
        elif req.model == "gemini":
            ai_provider = GeminiProvider()
        elif req.model == "claude":
             ai_provider = ClaudeProvider()
        else:
            raise ValueError("Unsupported model selected.")

        ai_reply = await ai_provider.get_response(req.message)  # <-- Use await
        return {"response": ai_reply}
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
