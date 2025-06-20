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

Sign in to https://openrouter.ai and navigate to keys at https://openrouter.ai/settings/keys
Then create an API key and save it

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

### 6. (optional) Customize web port
You can edit the app-llm.py file to customize web port, and more!

```py
if __name__ == "__main__":
    port = 5000
```

---

## License

[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

You may use, share, and adapt this project for non-commercial purposes with proper attribution. Commercial use is not permitted.
