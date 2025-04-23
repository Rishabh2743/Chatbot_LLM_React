import React, { useState,useRef ,useEffect } from "react";
import axios from "axios";
import './index.css';

function ChatbotUI() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [temp, setTemp] = useState("");
  const [loading, setLoading] = useState(false);
  const [model, setModel] = useState("gpt"); // default model
  const lastMessageRef = useRef(null); 

  const API_URL = "http://localhost:8000/send_message";
  

  const sendMessage = async () => {
    if (!input.trim()) return;

    setMessages([...messages, { sender: "user", text: input }]);
    setLoading(true);

    try {
      const response = await axios.post(API_URL, {
        message: input,
        model: model // send selected model
      });



      const aiReply = response.data.response || "Error: No response from API.";
      setMessages((prev) => [...prev, { sender: "ai", text: aiReply }]);
    } catch (error) {
      const errorMessage =
        error.response?.data?.detail || // Custom backend error message
        error.message ||                // Axios/network-level error
        "⚠️ Error: Could not reach the backend."; // Fallback
    
      setMessages((prev) => [
        ...prev,
        { sender: "ai", text: `⚠️ ${errorMessage}` },
      ]);
    } finally {
      setLoading(false);
      setInput("");
    }
  };

  
  useEffect(() => {
    if (lastMessageRef.current) {
      lastMessageRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [messages]);

  return (
    <div className="container">
      <h2 className="header">🤖 Chat with AI</h2>

      {/* LLM model selection dropdown */}
      <div className="model-select">
        <label htmlFor="model">Choose LLM:</label>
        <select id="model"   style={{ width: "150px" }} value={model} onChange={(e) => setModel(e.target.value)}>
        <option value="gemini">Google Gemini</option>
        <option value="gpt">OpenAI GPT</option>
        <option value="claude">Anthropic Claude</option>
          {/* Add more models here if needed */}
        </select>
      </div>

       <div className="chatbox">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`message ${msg.sender}`}
            ref={index === messages.length - 1 ? lastMessageRef : null} // Attach ref to last message
          >
            <p className="text">{msg.text}</p>
          </div>
        ))}
        {loading && <div className="typing">AI is typing...</div>}
      </div>

      <div className="input-area">
       <input
       type="text"
       value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type your message..."
         onKeyDown={(e) => {
          if (e.key === "Enter") {
            const userInput = input;
           setInput(""); 
           sendMessage(); }}}/>
          <button onClick={sendMessage}>Send</button>
       </div>
    </div>
  );
}

export default ChatbotUI;
