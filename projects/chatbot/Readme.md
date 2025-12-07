# 🤖 Local AI Assistant (Ollama + RAG + Voice + Code + PDF Export)

This is a **fully offline, multi-feature AI Assistant** built using:

- **Ollama (LLaMA3)** for local LLM inference  
- **Streamlit** for the web interface  
- **LangChain + FAISS** for PDF Question Answering (RAG)  
- **Vosk + SoundDevice** for offline Voice Input  
- **FPDF** for Chat Export to Professional PDF  

✅ No API keys  
✅ No internet required after setup  
✅ Unlimited usage  
✅ Runs completely on your local machine  

---

## 🚀 Features

- ✅ **General Chat** – Normal AI conversation
- ✅ **PDF Question Answering (RAG)** – Upload a PDF and ask questions from it
- ✅ **Voice Input (Offline)** – Talk to the AI using your microphone
- ✅ **Code Assistant Mode** – Works as a coding helper for:
  - Python
  - C
  - C++
  - Java
  - JavaScript
  - Go
- ✅ **Export Chat to PDF** – Clean, formatted, readable PDF output
- ✅ **Streaming Responses** – Live response generation
- ✅ **100% Offline AI System**

---

## 🖥️ System Requirements

- ✅ Linux OS (Tested on Ubuntu)
- ✅ Python **3.9+**
- ✅ Working Microphone (for voice input)
- ✅ Minimum **8 GB RAM** (recommended for LLaMA3)

---

## 🧠 Installation Guide

### ✅ Step 1: Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
````

Verify:

```bash
ollama --version
```

---

### ✅ Step 2: Download LLaMA3 Model

```bash
ollama run llama3
```

⚠️ Keep this terminal OPEN while using the app.

---

### ✅ Step 3: Create & Activate Virtual Environment

```bash
python3 -m venv env
source env/bin/activate
```

---

### ✅ Step 4: Install All Python Dependencies

```bash
pip install streamlit requests sounddevice scipy vosk \
           langchain langchain-community faiss-cpu fpdf pypdf
```

---

### ✅ Step 5: Install System Audio Dependencies (For Voice Input)

```bash
sudo apt update
sudo apt install -y portaudio19-dev python3-pyaudio
```

---

### ✅ Step 6: Download Vosk Speech Model

```bash
mkdir -p models
cd models
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
cd ..
```

Final path must be:

```
models/vosk-model-small-en-us-0.15/
```

---

## 📂 Project Structure

```
projects/
 └── chatbot/
     ├── app.py
     ├── uploads/
models/
env/
README.md
```

---

## ▶️ How To Run The Project

### ✅ Terminal 1 – Start Ollama

```bash
ollama run llama3
```

---

### ✅ Terminal 2 – Run Streamlit App

```bash
streamlit run projects/chatbot/app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧭 Usage Guide

### ✅ 1. General Chat

* Select: **General Chat**
* Type or speak your question

---

### ✅ 2. PDF Question Answering (RAG)

* Select: **PDF QA (RAG)**
* Upload a PDF
* Ask questions directly from the PDF

---

### ✅ 3. Voice Input

* Click: **🎤 Speak**
* Speak clearly for 6 seconds
* Your voice is converted to text and sent to the AI

---

### ✅ 4. Code Assistant Mode

* Select: **Code Assistant**
* Choose programming language
* Ask:

  * Debugging questions
  * Write new code
  * Optimize code
  * Explain logic

Example:

```
Write a Python function for checking prime numbers.
```

---

### ✅ 5. Export Chat to PDF

* After chatting, click:

  ```
  📄 Export chat to PDF
  ```
* A clean, readable `chat_history.pdf` will download

---

## 🛠 Tech Stack

* **LLM**: Ollama (LLaMA3)
* **Frontend**: Streamlit
* **RAG**: LangChain + FAISS
* **Voice Input**: Vosk + SoundDevice
* **PDF Export**: FPDF
* **Speech Recognition**: Offline, No Cloud
* **Vector Search**: FAISS

---

## ✅ Advantages Over Cloud AI

| Feature         | This Project | Cloud AI |
| --------------- | ------------ | -------- |
| Works Offline   | ✅ Yes        | ❌ No     |
| No API Key      | ✅ Yes        | ❌ No     |
| Unlimited Usage | ✅ Yes        | ❌ No     |
| Voice Input     | ✅ Yes        | ✅ Yes    |
| PDF QA (RAG)    | ✅ Yes        | ✅ Yes    |
| Cost            | ✅ Free       | ❌ Paid   |

---

## 🧯 Common Errors & Fixes

### ❌ Ollama not running

```bash
ollama run llama3
```

---

### ❌ Voice not working

```bash
sudo apt install portaudio19-dev
pip install sounddevice
```

---

### ❌ PDF not answering

* Ensure you uploaded the PDF
* Ask questions related to the document only

---

## 👨‍💻 Author

**Developed By:** Ashant Kumar
**Project:** Full Offline AI Assistant with Voice + RAG + Code + PDF

---

## ✅ Final Status

✅ General Chat – Working
✅ PDF QA (RAG) – Working
✅ Voice Input – Working
✅ Code Assistant – Working
✅ Clean PDF Export – Working
✅ Fully Offline AI Assistant – Completed Successfully

---

🔥 This project is now **portfolio-ready** and suitable for:

* Final year project
* Internship demos
* Research demos
* Resume showcase

