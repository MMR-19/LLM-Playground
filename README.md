# LLM-Playground
Playground for OpenRouter free LLM Models

---

## ✨ Features

- Small, lightweight, and easy to run
- Real-time chat with LLMs (system + user prompts)
- Automatically lists only **free models** from OpenRouter
- Built-in endpoint to check rate limits
- Uses Socket.IO for smooth frontend/backend communication

---

## 🚀 Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/MMR-19/LLM-Playground.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create an API key on OpenRouter.ai

Sign in to https://openrouter.ai and navigate to keys (https://openrouter.ai/settings/keys). Then create an API key and copy it

### 4. Replace your API key on .env file

```txt
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

⚠️ Note: Using a .env file is fine for development, but don't use it in production without securing it properly

### 5. Run the app

```bash
python app-llm.py
```

This should open your browser automatically on http://localhost:5000

PS: You can edit the app-llm.py file to customize web port, and more!

