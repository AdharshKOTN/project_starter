# Project Starter

A set of scripts and applications that help automate the building/initializing code repositories leveraging LLMs for content and structure suggestions.

## How to run this Program

Start command: python main.py

Project Name - Text Field ( compatible to underlying file system )
Project Type - Flask ( Currently Supported )
LLM use      - Use of CodeLLama or gpt-4o-mini ( requires paid subscription service on openAI site )

## 🧠 Running This Project Starter with Ollama (Linux/macOS)

This app supports local LLM generation using [Ollama](https://ollama.com), allowing you to scaffold projects even without OpenAI API access.

### ✅ Step 1: Install Ollama

#### On macOS:
```bash
brew install ollama
```

#### On Linux:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

### 🚀 Step 2: Run a Local LLM

We recommend using [CodeLlama](https://ollama.com/library/codellama) or [Mistral](https://ollama.com/library/mistral) for project generation:

```bash
ollama run codellama
```

Ollama will download the model (if not already installed) and begin running it locally.

---

### 🧪 Step 3: Install the Python Ollama Client

Inside your Python environment:

```bash
pip install ollama
```

---

### 🧠 Step 4: You’re Ready!

The `project_starter` app will automatically use Ollama if you choose the local LLM option when prompted.

> ⚠️ **Note:** The first model run will require a download (~3–8GB). Make sure you have enough disk space and memory (8GB+ RAM recommended). 