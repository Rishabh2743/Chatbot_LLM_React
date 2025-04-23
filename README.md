# Chatbot UI Frontend

This project is a React-based chatbot UI that allows users to interact with various AI models like OpenAI GPT, Google Gemini, and Anthropic Claude.

## Installation

Follow these steps to set up and run the frontend.

```bash
cd frontend
npm install
npm install axios
npm start


#The server will be available at:
http://localhost:3000/



# Chatbot Backend
This is the backend for the Chatbot UI, built with FastAPI. It connects to OpenAI GPT, Google Gemini, and Anthropic Claude to provide intelligent responses.

---

## 🔧 Installation

### 1. Clone the Repo

```bash
cd backend
pip install -r requirements.txt
pip install fastapi uvicorn openai google-generativeai anthropic anyio python-dotenv


#Create a .env file in the root folder:
OPENAI_API_KEY=key
GEMINI_API_KEY=key
CLAUDE_API_KEY=

#Run the FastAPI server with:
```bash
uvicorn main:app --reload

#The server will be available at:
📍 http://127.0.0.1:8000

#Swagger docs available at:
📘 http://127.0.0.1:8000/docs

#POST /send_message
Request:
json
Copy
Edit
{
  "message": "Hello!",
  "model": "gpt"   // Options: "gpt", "gemini", "claude"
}
#Response:
json
Copy
Edit
{
  "response": "Hi! How can I help you today?"
}