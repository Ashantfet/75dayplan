# # # import streamlit as st
# # # import requests

# # # st.set_page_config(page_title="Local AI Chatbot", layout="centered")

# # # st.title("✅ Local AI Chatbot (Ollama + LLaMA3)")

# # # if "history" not in st.session_state:
# # #     st.session_state.history = []

# # # user_input = st.text_input("Ask anything:")

# # # if user_input:
# # #     st.session_state.history.append(("You", user_input))

# # #     try:
# # #         response = requests.post(
# # #             "http://localhost:11434/api/generate",
# # #             json={
# # #                 "model": "llama3",   # or "phi3"
# # #                 "prompt": user_input,
# # #                 "stream": False
# # #             }
# # #         )

# # #         ai_text = response.json()["response"]
# # #         st.session_state.history.append(("AI", ai_text))

# # #     except Exception as e:
# # #         st.error("❌ Ollama is not running. Start it with: ollama run llama3")
# # #         st.stop()

# # # # Display chat history
# # # for role, msg in st.session_state.history:
# # #     if role == "You":
# # #         st.markdown(f"🧑 **You:** {msg}")
# # #     else:
# # #         st.markdown(f"🤖 **AI:** {msg}")


# # import streamlit as st
# # import requests
# # import json

# # st.set_page_config(page_title="Local AI Chatbot", layout="centered")

# # st.title("✅ Local AI Chatbot (Ollama Pro)")

# # # -------------------------------
# # # Sidebar Settings
# # # -------------------------------
# # st.sidebar.title("⚙️ Settings")

# # # model_name = st.sidebar.selectbox(
# # #     "Choose Model",
# # #     ["llama3", "phi3", "mistral"]
# # # )
# # model_name = "llama3"
# # st.sidebar.markdown("### 🧠 Model Used")
# # st.sidebar.success("LLaMA 3 (Fixed)")

# # if st.sidebar.button("🗑️ Clear Chat"):
# #     st.session_state.history = []

# # # -------------------------------
# # # Initialize Chat History
# # # -------------------------------
# # if "history" not in st.session_state:
# #     st.session_state.history = []

# # # -------------------------------
# # # Display Chat History
# # # -------------------------------
# # for role, msg in st.session_state.history:
# #     if role == "You":
# #         st.markdown(f"🧑 **You:** {msg}")
# #     else:
# #         st.markdown(f"🤖 **AI:** {msg}")

# # # -------------------------------
# # # User Input
# # # -------------------------------
# # user_input = st.text_input("Ask anything:")

# # if user_input:
# #     st.session_state.history.append(("You", user_input))
# #     ai_placeholder = st.empty()

# #     try:
# #         response = requests.post(
# #             "http://localhost:11434/api/generate",
# #             json={
# #                 "model": model_name,
# #                 "prompt": user_input,
# #                 "stream": True
# #             },
# #             stream=True,
# #             timeout=300
# #         )

# #         full_text = ""

# #         for line in response.iter_lines():
# #             if line:
# #                 data = json.loads(line.decode("utf-8"))  # ✅ SAFE JSON PARSE
# #                 token = data.get("response", "")
# #                 full_text += token
# #                 ai_placeholder.markdown(f"🤖 **AI:** {full_text}")

# #         st.session_state.history.append(("AI", full_text))

# #     except requests.exceptions.ConnectionError:
# #         st.error("❌ Ollama is not running. Start it with: ollama run llama3")
# #     except Exception as e:
# #         st.error(f"❌ Error: {e}")


# # import streamlit as st
# # import requests
# # import json
# # import os
# # from langchain_community.document_loaders import PyPDFLoader
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # from langchain_community.vectorstores import FAISS
# # from langchain.embeddings.base import Embeddings

# # # -------------------------------
# # # Ollama Embeddings (Local)
# # # -------------------------------
# # class OllamaEmbeddings(Embeddings):
# #     def embed_documents(self, texts):
# #         embeddings = []
# #         for text in texts:
# #             response = requests.post(
# #                 "http://localhost:11434/api/embeddings",
# #                 json={"model": "llama3", "prompt": text}
# #             )
# #             embeddings.append(response.json()["embedding"])
# #         return embeddings

# #     def embed_query(self, text):
# #         response = requests.post(
# #             "http://localhost:11434/api/embeddings",
# #             json={"model": "llama3", "prompt": text}
# #         )
# #         return response.json()["embedding"]

# # # -------------------------------
# # # Streamlit Config
# # # -------------------------------
# # st.set_page_config(page_title="AI Assistant (RAG)", layout="centered")
# # st.title("✅ Local AI Assistant (Ollama + RAG)")

# # # -------------------------------
# # # Sidebar Features
# # # -------------------------------
# # st.sidebar.header("📂 Document QA (RAG)")
# # uploaded_file = st.sidebar.file_uploader("Upload a PDF", type=["pdf"])

# # # -------------------------------
# # # Initialize Session State
# # # -------------------------------
# # if "vector_db" not in st.session_state:
# #     st.session_state.vector_db = None

# # if "pdf_name" not in st.session_state:
# #     st.session_state.pdf_name = None

# # # -------------------------------
# # # Load PDF & Create Vector Store (ONLY ONCE)
# # # -------------------------------
# # if uploaded_file and st.session_state.pdf_name != uploaded_file.name:

# #     os.makedirs("projects/chatbot/uploads", exist_ok=True)

# #     pdf_path = f"projects/chatbot/uploads/{uploaded_file.name}"
# #     with open(pdf_path, "wb") as f:
# #         f.write(uploaded_file.read())

# #     loader = PyPDFLoader(pdf_path)
# #     documents = loader.load()

# #     splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
# #     chunks = splitter.split_documents(documents)

# #     embeddings = OllamaEmbeddings()
# #     vector_db = FAISS.from_documents(chunks, embeddings)

# #     # ✅ STORE IN SESSION (THIS IS THE FIX)
# #     st.session_state.vector_db = vector_db
# #     st.session_state.pdf_name = uploaded_file.name

# #     st.sidebar.success("✅ PDF processed and cached successfully!")

# # # -------------------------------
# # # Chat History
# # # -------------------------------
# # if "history" not in st.session_state:
# #     st.session_state.history = []

# # for role, msg in st.session_state.history:
# #     if role == "You":
# #         st.markdown(f"🧑 **You:** {msg}")
# #     else:
# #         st.markdown(f"🤖 **AI:** {msg}")

# # # -------------------------------
# # # User Input
# # # -------------------------------
# # user_input = st.text_input("Ask normally OR ask from your PDF:")

# # if user_input:
# #     st.session_state.history.append(("You", user_input))
# #     ai_placeholder = st.empty()

# #     try:
# #         # ✅ RAG MODE (USE STORED VECTOR DB)
# #         if st.session_state.vector_db is not None:
# #             docs = st.session_state.vector_db.similarity_search(user_input, k=3)
# #             context = "\n".join([doc.page_content for doc in docs])

# #             prompt = f"""
# #             Answer ONLY from the context below:

# #             {context}

# #             Question: {user_input}
# #             """

# #         else:
# #             prompt = user_input

# #         response = requests.post(
# #             "http://localhost:11434/api/generate",
# #             json={
# #                 "model": "llama3",
# #                 "prompt": prompt,
# #                 "stream": True
# #             },
# #             stream=True
# #         )

# #         full_text = ""
# #         for line in response.iter_lines():
# #             if line:
# #                 data = json.loads(line.decode("utf-8"))
# #                 token = data.get("response", "")
# #                 full_text += token
# #                 ai_placeholder.markdown(f"🤖 **AI:** {full_text}")

# #         st.session_state.history.append(("AI", full_text))

# #     except Exception:
# #         st.error("❌ Ollama is not running. Start it with: ollama run llama3")


# import streamlit as st
# import requests
# import json
# import os
# import sounddevice as sd
# import scipy.io.wavfile as wav
# from vosk import Model, KaldiRecognizer

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import FAISS
# from langchain.embeddings.base import Embeddings

# # -------------------------------
# # CONFIG
# # -------------------------------
# OLLAMA_URL = "http://localhost:11434"
# MODEL_NAME = "llama3"
# VOSK_MODEL_PATH = "models/vosk-model-small-en-us-0.15"

# # -------------------------------
# # Load Vosk Model ONCE
# # -------------------------------
# if "vosk_model" not in st.session_state:
#     st.session_state.vosk_model = Model(VOSK_MODEL_PATH)

# # -------------------------------
# # Ollama Embeddings (Local)
# # -------------------------------
# class OllamaEmbeddings(Embeddings):
#     def embed_documents(self, texts):
#         embeddings = []
#         for text in texts:
#             r = requests.post(
#                 f"{OLLAMA_URL}/api/embeddings",
#                 json={"model": MODEL_NAME, "prompt": text}
#             )
#             embeddings.append(r.json()["embedding"])
#         return embeddings

#     def embed_query(self, text):
#         r = requests.post(
#             f"{OLLAMA_URL}/api/embeddings",
#             json={"model": MODEL_NAME, "prompt": text}
#         )
#         return r.json()["embedding"]

# # -------------------------------
# # Streamlit Config
# # -------------------------------
# st.set_page_config(page_title="AI Assistant (RAG + Voice)", layout="centered")
# st.title("✅ Local AI Assistant (Ollama + RAG + Voice)")

# # -------------------------------
# # Sidebar - PDF Upload
# # -------------------------------
# st.sidebar.header("📂 Document QA (RAG)")
# uploaded_file = st.sidebar.file_uploader("Upload a PDF", type=["pdf"])

# # -------------------------------
# # SESSION STATE INIT
# # -------------------------------
# if "vector_db" not in st.session_state:
#     st.session_state.vector_db = None

# if "pdf_name" not in st.session_state:
#     st.session_state.pdf_name = None

# if "history" not in st.session_state:
#     st.session_state.history = []

# # -------------------------------
# # Load PDF & Create Vector Store (Cached)
# # -------------------------------
# if uploaded_file and st.session_state.pdf_name != uploaded_file.name:

#     os.makedirs("projects/chatbot/uploads", exist_ok=True)

#     pdf_path = f"projects/chatbot/uploads/{uploaded_file.name}"
#     with open(pdf_path, "wb") as f:
#         f.write(uploaded_file.read())

#     loader = PyPDFLoader(pdf_path)
#     documents = loader.load()

#     splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
#     chunks = splitter.split_documents(documents)

#     embeddings = OllamaEmbeddings()
#     st.session_state.vector_db = FAISS.from_documents(chunks, embeddings)
#     st.session_state.pdf_name = uploaded_file.name

#     st.sidebar.success("✅ PDF processed & cached!")

# # -------------------------------
# # Display Chat History
# # -------------------------------
# for role, msg in st.session_state.history:
#     if role == "You":
#         st.markdown(f"🧑 **You:** {msg}")
#     else:
#         st.markdown(f"🤖 **AI:** {msg}")

# # -------------------------------
# # TEXT INPUT
# # -------------------------------
# user_input = st.text_input("Type your question:")

# # -------------------------------
# # VOICE INPUT (PORTAUDIO SAFE)
# # -------------------------------
# if "listening" not in st.session_state:
#     st.session_state.listening = False

# if st.button("🎤 Speak"):
#     st.session_state.listening = True

# if st.session_state.listening:
#     st.warning("🎙️ Recording for 6 seconds... Speak clearly!")

#     fs = 48000      # ✅ More compatible sample rate
#     duration = 6
#     channels = 1    # ✅ Mono (most stable)

#     try:
#         recording = sd.rec(
#             int(duration * fs),
#             samplerate=fs,
#             channels=channels,
#             dtype="int16"   # ✅ Critical fix
#             # ✅ No device param → use default safely
#         )
#         sd.wait()

#         wav.write("voice.wav", fs, recording)

#         rec = KaldiRecognizer(st.session_state.vosk_model, fs)

#         with open("voice.wav", "rb") as f:
#             audio_data = f.read()
#             if rec.AcceptWaveform(audio_data):
#                 result = json.loads(rec.Result())
#                 voice_text = result.get("text", "").strip()
#             else:
#                 final = json.loads(rec.FinalResult())
#                 voice_text = final.get("text", "").strip()

#         if voice_text:
#             st.success(f"✅ You said: {voice_text}")
#             user_input = voice_text
#             st.session_state.history.append(("You", voice_text))
#         else:
#             st.error("❌ Voice captured but speech not clear. Try again slowly.")

#     except Exception as e:
#         st.error("❌ Microphone stream error. Try restarting audio system.")
#         st.code(str(e))

#     st.session_state.listening = False



# # -------------------------------
# # PROCESS INPUT (TEXT OR VOICE)
# # -------------------------------
# if user_input:

#     if not st.session_state.history or st.session_state.history[-1][1] != user_input:
#         st.session_state.history.append(("You", user_input))

#     ai_placeholder = st.empty()

#     # ✅ RAG or Normal Mode
#     if st.session_state.vector_db is not None:
#         docs = st.session_state.vector_db.similarity_search(user_input, k=3)
#         context = "\n".join([doc.page_content for doc in docs])

#         prompt = f"""
#         Answer ONLY from the context below:

#         {context}

#         Question: {user_input}
#         """
#     else:
#         prompt = user_input

#     try:
#         response = requests.post(
#             f"{OLLAMA_URL}/api/generate",
#             json={"model": MODEL_NAME, "prompt": prompt, "stream": True},
#             stream=True,
#             timeout=300
#         )

#         full_text = ""

#         for line in response.iter_lines():
#             if line:
#                 data = json.loads(line.decode("utf-8"))
#                 token = data.get("response", "")
#                 full_text += token
#                 ai_placeholder.markdown(f"🤖 **AI:** {full_text}")

#         st.session_state.history.append(("AI", full_text))

#     except Exception:
#         st.error("❌ Ollama is not running. Start it with: ollama run llama3")


import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # avoid CUDA noise

import streamlit as st
import requests
import json
import sounddevice as sd
import scipy.io.wavfile as wav
from vosk import Model, KaldiRecognizer

from fpdf import FPDF

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings.base import Embeddings

# -------------------------------
# CONFIG
# -------------------------------
OLLAMA_URL = "http://localhost:11434"
LLM_MODEL = "llama3"
VOSK_MODEL_PATH = "models/vosk-model-small-en-us-0.15"

UPLOAD_DIR = "projects/chatbot/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# -------------------------------
# Load Vosk Model ONCE
# -------------------------------
if "vosk_model" not in st.session_state:
    st.session_state.vosk_model = Model(VOSK_MODEL_PATH)

# -------------------------------
# Ollama Embeddings (Local)
# -------------------------------
class OllamaEmbeddings(Embeddings):
    def embed_documents(self, texts):
        embeddings = []
        for text in texts:
            r = requests.post(
                f"{OLLAMA_URL}/api/embeddings",
                json={"model": LLM_MODEL, "prompt": text}
            )
            embeddings.append(r.json()["embedding"])
        return embeddings

    def embed_query(self, text):
        r = requests.post(
            f"{OLLAMA_URL}/api/embeddings",
            json={"model": LLM_MODEL, "prompt": text}
        )
        return r.json()["embedding"]


from datetime import datetime
from fpdf import FPDF
import re
import textwrap

def clean_markdown(text: str) -> str:
    # Remove markdown bold, italics, code fences
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"`{3}", "", text)
    return text.strip()


def chat_to_pdf_bytes(history):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # ---------- TITLE ----------
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "AI Chat History", ln=True, align="C")
    pdf.ln(2)

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 8, f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}", ln=True, align="C")
    pdf.ln(10)

    # ---------- CONTENT ----------
    for role, msg in history:
        msg = clean_markdown(msg)

        # ✅ Role Header
        if role == "You":
            pdf.set_font("Arial", "B", 12)
            pdf.set_text_color(0, 0, 120)
            pdf.cell(0, 8, "You:", ln=True)
        else:
            pdf.set_font("Arial", "B", 12)
            pdf.set_text_color(120, 0, 0)
            pdf.cell(0, 8, "AI:", ln=True)

        pdf.ln(1)

        # ✅ Detect CODE vs NORMAL text
        is_code = msg.strip().startswith(("class ", "def ", "import ", "for ", "while "))

        if is_code:
            # ✅ Proper monospace code block
            pdf.set_font("Courier", size=10)
            pdf.set_text_color(20, 20, 20)

            lines = msg.split("\n")
            for line in lines:
                pdf.multi_cell(0, 6, line.rstrip())

        else:
            # ✅ Normal wrapped paragraph
            pdf.set_font("Arial", size=11)
            pdf.set_text_color(40, 40, 40)

            paragraphs = msg.split("\n")
            for para in paragraphs:
                wrapped_lines = textwrap.wrap(para, width=90)
                if not wrapped_lines:
                    pdf.ln(4)
                for w in wrapped_lines:
                    pdf.multi_cell(0, 6, w)

        # ✅ Section Divider
        pdf.ln(4)
        pdf.set_draw_color(180, 180, 180)
        pdf.line(12, pdf.get_y(), 198, pdf.get_y())
        pdf.ln(6)

    return pdf.output(dest="S").encode("latin-1")




# -------------------------------
# Streamlit Config
# -------------------------------
st.set_page_config(page_title="Local AI Assistant", layout="centered")
st.title("✅ Local AI Assistant (Ollama + RAG + Voice + Code)")


# -------------------------------
# Sidebar: Modes & PDF Upload
# -------------------------------
st.sidebar.header("🧠 Assistant Mode")
mode = st.sidebar.radio(
    "Choose mode:",
    ["General Chat", "PDF QA (RAG)", "Code Assistant"],
)

st.sidebar.markdown("---")
st.sidebar.header("📂 Document QA (RAG)")

uploaded_file = None
if mode == "PDF QA (RAG)":
    uploaded_file = st.sidebar.file_uploader("Upload a PDF", type=["pdf"])

st.sidebar.markdown("---")

# -------------------------------
# Sidebar: Code Assistant Settings
# -------------------------------
code_language = None
if mode == "Code Assistant":
    st.sidebar.header("💻 Code Settings")
    code_language = st.sidebar.selectbox(
        "Language",
        ["Python", "C++", "Java", "JavaScript", "C", "Go"],
    )

st.sidebar.markdown("---")

# Export chat to PDF button
if "history" not in st.session_state:
    st.session_state.history = []

if st.session_state.history:
    pdf_bytes = chat_to_pdf_bytes(st.session_state.history)
    st.sidebar.download_button(
        label="📄 Export chat to PDF",
        data=pdf_bytes,
        file_name="chat_history.pdf",
        mime="application/pdf",
    )

# -------------------------------
# Session State Init for RAG
# -------------------------------
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = None

# -------------------------------
# Load PDF & Create Vector Store (Cached)
# -------------------------------
if uploaded_file and st.session_state.pdf_name != uploaded_file.name:

    pdf_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    embeddings = OllamaEmbeddings()
    st.session_state.vector_db = FAISS.from_documents(chunks, embeddings)
    st.session_state.pdf_name = uploaded_file.name

    st.sidebar.success("✅ PDF processed & cached!")


# -------------------------------
# Display Chat History
# -------------------------------
for role, msg in st.session_state.history:
    if role == "You":
        st.markdown(f"🧑 **You:** {msg}")
    else:
        st.markdown(f"🤖 **AI:** {msg}")


# -------------------------------
# Text Input
# -------------------------------
placeholder_label = {
    "General Chat": "Type your question:",
    "PDF QA (RAG)": "Ask a question based on the uploaded PDF:",
    "Code Assistant": "Describe the code task / bug / question:",
}[mode]

user_input = st.text_input(placeholder_label)


# -------------------------------
# VOICE INPUT (works for all modes)
# -------------------------------
if "listening" not in st.session_state:
    st.session_state.listening = False

if st.button("🎤 Speak"):
    st.session_state.listening = True

if st.session_state.listening:
    st.warning("🎙️ Recording for 6 seconds... Speak clearly!")

    fs = 48000
    duration = 6
    channels = 1

    try:
        recording = sd.rec(
            int(duration * fs),
            samplerate=fs,
            channels=channels,
            dtype="int16",
        )
        sd.wait()

        wav.write("voice.wav", fs, recording)

        rec = KaldiRecognizer(st.session_state.vosk_model, fs)

        with open("voice.wav", "rb") as f:
            audio_data = f.read()
            if rec.AcceptWaveform(audio_data):
                result = json.loads(rec.Result())
                voice_text = result.get("text", "").strip()
            else:
                final = json.loads(rec.FinalResult())
                voice_text = final.get("text", "").strip()

        if voice_text:
            st.success(f"✅ You said: {voice_text}")
            user_input = voice_text
            st.session_state.history.append(("You", voice_text))
        else:
            st.error("❌ Voice captured but speech not recognized. Try again.")

    except Exception as e:
        st.error("❌ Microphone stream error.")
        st.code(str(e))

    st.session_state.listening = False


# -------------------------------
# Handle Input (Text or Voice)
# -------------------------------
if user_input:
    # Avoid double-adding if already added by voice block
    if not st.session_state.history or st.session_state.history[-1][1] != user_input:
        st.session_state.history.append(("You", user_input))

    ai_placeholder = st.empty()

    # --- Build prompt based on mode ---
    if mode == "PDF QA (RAG)" and st.session_state.vector_db is not None:
        docs = st.session_state.vector_db.similarity_search(user_input, k=3)
        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are a precise assistant answering ONLY from the given document context.

CONTEXT:
{context}

QUESTION:
{user_input}

If the answer is not in the context, say you don't know based on this document.
"""
    elif mode == "Code Assistant":
        lang = code_language or "Python"
        prompt = f"""
You are an expert {lang} coding assistant.

User's request:
{user_input}

Requirements:
- If user asks for code, provide {lang} code with clear comments.
- If user asks to debug, explain the bug and show the fixed code.
- If user asks to optimize, explain the changes and why they help.
- Keep explanations clear and practical.
"""
    else:  # General Chat
        prompt = user_input

    # --- Call Ollama ---
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={"model": LLM_MODEL, "prompt": prompt, "stream": True},
            stream=True,
            timeout=300,
        )

        full_text = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                token = data.get("response", "")
                full_text += token
                ai_placeholder.markdown(f"🤖 **AI:** {full_text}")

        st.session_state.history.append(("AI", full_text))

    except Exception:
        st.error("❌ Ollama is not running. Start it with: `ollama run llama3`")
