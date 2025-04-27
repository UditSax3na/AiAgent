# Multi-Language Code Runner with AI Integration

A cross-platform Python utility that detects and runs code files written in multiple programming languages, with built-in support for CLI interaction using Typer and AI integration via OpenRouter (OpenAI-compatible APIs).

Note:
The ai-agent folder contains an unfinished VS Code extension. If you're familiar with creating or using VS Code extensions, feel free to build upon it and improve it. 

---

## Features

- Supports **Python, Java, C, C++, JavaScript, TypeScript, Go, Rust, Ruby, PHP, Bash, Perl**
- Detects language automatically by file extension
- Integrates **AI models** (via OpenRouter & OpenAI-compatible APIs)
- Works seamlessly on **Windows, macOS, and Linux**
- Built with **Typer** for an elegant CLI experience
- Uses `.env` for secure environment variable handling

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/UditSax3na/AiAgent.git
cd AiAgent
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Add Environment Variables
```bash
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

---
# Requirements
### Install required Library/ Modules/Packages

```bash
pip install -r requirements.txt
```

### Requirements (requirement.txt)
```
typer
openai
python-dotenv
```
---
## Usage

### Run a Code File
```bash
python main.py
```
---

### Author
made by :- [UditSax3na](https://github.com/UditSax3na)
