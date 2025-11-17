# AI Agent Project

A lightweight conversational AI agent built using **Google Gemini (genai API)** with:

- Chat conversation with memory  
- Tool execution (Calculator tool included)  
- Auto language detection (agent replies in same language)  
- Simple CLI interface  
- Easy to extend with more tools  

---

## 🚀 Features

- **Gemini-powered chat agent** using `gemini-2.5-flash`
- **Memory module** storing last 8 messages
- **Tool system**
- **System prompt** ensuring clear, language-matched responses
- **CLI chat loop** for interactive use

---

## 🔧 Setup

### Add your API key
Inside `aiagent.py`, replace:
```python
api_key = "YOUR_API_KEY"
```

---

## ▶️ How to Run

Start the AI Agent:
```bash
python aiagent.py
```

You will see:
```
Gemini AI Agent Ready!
You:
```

Start chatting!

---

## 🛠 Tool Usage

Use calculator tool:
```
use:calculator{5*7}
```

Output:
```
Result / ফলাফল: 35
```

---

### Chat Example:
```
You: Hello
Agent: Hello! How can I assist you today?
```

### Tool Example:
```
You: use:calculator{10/2}
Agent: Result / ফলাফল: 5.0
```

---

## 💡 How It Works (Internally)

1. Takes user input  
2. Detects if it's a tool command  
3. If tool → executes tool  
4. If not → sends prompt + memory to Gemini API  
5. Receives and returns output  
6. Saves both user & assistant messages in memory  

---

## 📌 Future Improvements

- Add more tools (web search, translators, file tools)  
- Add GUI interface  
- Add persistent memory  
- Add API server version  

---

## 📜 License

Free to use for learning and development.

