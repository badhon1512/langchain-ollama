# 🚀 LLM API Scripts with LangChain & Streamlit

This repository contains a Streamlit-based chatbot that interacts with two powerful language models:  
- **DeepSeek V1.5B**  
- **GPT-3.5 Turbo**  

The implementation leverages `LangChain` for prompt handling, `Ollama` for running local models, and `Streamlit` for a simple web-based interface.

---

## 📌 Description  
This project provides a chatbot interface that interacts with **DeepSeek V1.5B** using **LangChain** and **Ollama**. The script:  
- Loads environment variables using `dotenv`.  
- Sets up a prompt template for structured interactions.  
- Uses `Ollama` to load **DeepSeek V1.5B** / **GPT-3.5 Turbo** locally.  
- Creates a processing chain to generate responses.  
- Provides a `Streamlit`-based web UI for user interaction.

## 🛠️ Installation & Setup

1. Download and install Ollama from:🔗 https://ollama.com
2. Setup your api key in .env
3. For running deepseekr1 run deepseek locally: ollama run deepseek-r1:1.5b 
