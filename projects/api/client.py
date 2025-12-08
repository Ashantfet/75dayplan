# # import requests
# # import streamlit as st

# # def get_ollama_response_essay(input_text):
# #     response=requests.post("http://localhost:8000/essay/invoke",
# #     json={'input':{'topic':input_text}})

# #     return response.json()['output']['content']

# # def get_ollama_response_poem(input_text):
# #     response=requests.post(
# #     "http://localhost:8000/poem/invoke",
# #     json={'input':{'topic':input_text}})

# #     return response.json()['output']['content']

# #     ## streamlit framework

# # st.title('Langchain Demo With LLAMA2 API')
# # input_text=st.text_input("Write an essay on")
# # input_text1=st.text_input("Write a poem on")

# # if input_text:
# #     st.write(get_ollama_response_essay(input_text))

# # if input_text1:
# #     st.write(get_ollama_response_poem(input_text1))

# import requests

# BASE_URL = "http://localhost:8000"

# # ----------------------------
# # Test General Chat
# # ----------------------------
# def test_chat():
#     print("\n🔹 Testing /chat route...")
    
#     payload = {
#         "input": "Explain artificial intelligence in simple words."
#     }

#     response = requests.post(f"{BASE_URL}/chat/invoke", json=payload)
#     result = response.json()

#     print("✅ Chat Response:\n")
#     print(result["output"])
#     print("-" * 60)


# # ----------------------------
# # Test Essay Generator
# # ----------------------------
# def test_essay():
#     print("\n🔹 Testing /essay route...")
    
#     payload = {
#         "input": {
#             "topic": "Machine Learning"
#         }
#     }

#     response = requests.post(f"{BASE_URL}/essay/invoke", json=payload)
#     result = response.json()

#     print("✅ Essay Response:\n")
#     print(result["output"])   # ✅ FIXED
#     print("-" * 60)


# # ----------------------------
# # Test Poem Generator
# # ----------------------------
# def test_poem():
#     print("\n🔹 Testing /poem route...")
    
#     payload = {
#         "input": {
#             "topic": "The Moon"
#         }
#     }

#     response = requests.post(f"{BASE_URL}/poem/invoke", json=payload)
#     result = response.json()

#     print("✅ Poem Response:\n")
#     print(result["output"])   # ✅ CORRECT
#     print("-" * 60)


# # ----------------------------
# # MAIN
# # ----------------------------
# if __name__ == "__main__":
#     print("\n🚀 Testing LangChain + Ollama API Server\n")

#     test_chat()
#     test_essay()
#     test_poem()

#     print("\n✅ All API routes tested successfully!\n")

import requests
import streamlit as st

BASE_URL = "http://localhost:8000"

st.set_page_config(page_title="LLaMA API Client", layout="centered")
st.title("🦙 LLaMA LangChain API – Streamlit Client")

st.markdown("Test all API routes powered only by **Ollama (llama3)**")

# -------------------------------
# MODE SELECTION
# -------------------------------
mode = st.selectbox(
    "Choose API Route to Test",
    ["Chat", "Essay Generator", "Poem Generator"]
)

st.markdown("---")

# -------------------------------
# CHAT MODE
# -------------------------------
if mode == "Chat":
    st.subheader("💬 General Chat  (/chat)")
    
    user_text = st.text_input("Ask anything:")

    if st.button("Send"):
        if user_text:
            payload = {"input": user_text}

            response = requests.post(
                f"{BASE_URL}/chat/invoke",
                json=payload
            )

            result = response.json()

            st.success("✅ Response:")
            st.write(result["output"])   # ✅ STRING OUTPUT (Ollama)

# -------------------------------
# ESSAY MODE
# -------------------------------
elif mode == "Essay Generator":
    st.subheader("📝 Essay Generator  (/essay)")
    
    topic = st.text_input("Enter topic for essay:")

    if st.button("Generate Essay"):
        if topic:
            payload = {
                "input": {
                    "topic": topic
                }
            }

            response = requests.post(
                f"{BASE_URL}/essay/invoke",
                json=payload
            )

            result = response.json()

            st.success("✅ Generated Essay:")
            st.write(result["output"])   # ✅ FIXED (NO ["content"])

# -------------------------------
# POEM MODE
# -------------------------------
elif mode == "Poem Generator":
    st.subheader("🎵 Poem Generator  (/poem)")
    
    topic = st.text_input("Enter topic for poem:")

    if st.button("Generate Poem"):
        if topic:
            payload = {
                "input": {
                    "topic": topic
                }
            }

            response = requests.post(
                f"{BASE_URL}/poem/invoke",
                json=payload
            )

            result = response.json()

            st.success("✅ Generated Poem:")
            st.write(result["output"])   # ✅ STRING OUTPUT
