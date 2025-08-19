# 🤖 AI Voice Assistant (Web UI)

A voice-based AI assistant built with **Streamlit**, **LangChain**, and **Ollama LLMs**
Speak to the assistant, get AI responses, and have it speak back to you in real-time.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/MaddyRizvi/ai-voice-assistant-web-ui.git
cd ai-voice-assistant
```

---

### 2️⃣ Install Dependencies
Create a virtual environment (recommended) and install required packages:
```bash
pip install -r requirements.txt
```

#### Example `requirements.txt`
```text
streamlit
speechrecognition
pyttsx3
langchain-community
langchain-core
langchain-ollama
pyaudio  # may require system-level installation
```

⚠️ **Note**:  
- Installing `pyaudio` on Windows may require a precompiled wheel.  
- Ollama must be installed locally for LLM inference. See [Ollama](https://ollama.ai/) for instructions.

---

### 3️⃣ Run the App
Start the Streamlit app:
```bash
streamlit run ai_voice_assistant.py
```
Open your browser at **http://localhost:8501** to interact with your AI assistant.

---

## 🖼️ Demo
<img width="1361" height="625" alt="Image" src="https://github.com/user-attachments/assets/e20fc657-6ca8-4274-b829-b4329431bc4f" />

---

## 🔧 How It Works
1. **Listen**: Captures microphone input and converts speech → text (`SpeechRecognition`).  
2. **Prompting**: Combines chat history with the current query and sends it to the LLM (`OllamaLLM`).  
3. **Response**: Generates AI text response.  
4. **Speak**: Reads out AI response using `pyttsx3`.  
5. **History**: Saves user and AI messages in `ChatMessageHistory` and displays them in the UI.

---

## 📦 Project Structure
```text
ai-voice-assistant/
│
├── ai_voice_assistant.py   # Main Streamlit app
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── demo.png                # Optional screenshot/GIF
```

---

## 🛠️ Tech Stack
- Python 3.9+  
- Streamlit  
- LangChain (chat history & prompts)  
- Ollama (local LLM inference)  
- SpeechRecognition (Google Web API)  
- pyttsx3 (offline text-to-speech)  

---

## 💡 Future Improvements
- 🌐 Multi-language support for speech recognition and TTS  
- 🎵 More natural voices (e.g., `gTTS` or ElevenLabs)  
- 🔗 Integrate external APIs (weather, Wikipedia, etc.)  
- 💾 Save/export chat history

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!  
Feel free to fork the repo, open a PR, or start a discussion.

---

## 📜 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

