from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llm.openai_provider import OpenAIProvider
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize FastAPI app
app = FastAPI()

# Retrieve the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')  # Fetches the key from the .env file
logging.info(f"API key detected? {'YES' if api_key else 'NO'}")

# Check if the API key is present
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize OpenAIProvider with the API key
ai_provider = OpenAIProvider(api_key)

# Request schema
class MessageRequest(BaseModel):
    message: str

# Response schema
class MessageResponse(BaseModel):
    response: str

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Chatbot API!"}

# POST endpoint to send message to OpenAI
@app.post("/send_message", response_model=MessageResponse)
async def send_message(req: MessageRequest):
    try:
        ai_reply = await ai_provider.get_response(req.message)
        return {"response": ai_reply}
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Favicon endpoint (optional)
@app.get("/favicon.ico")
async def favicon():
    favicon_path = "static/favicon.ico"  # Change this path if you have a custom favicon
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path)
    return FileResponse('favicon.ico')  # Return default icon if not found
