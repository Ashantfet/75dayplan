from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama

# ----- FASTAPI APP -----
app = FastAPI(
    title="LangChain Ollama API Server",
    version="1.0",
    description="A Production-Ready Offline LLaMA API Server"
)

# ----- OLLAMA MODEL (ONLY) -----
llm = Ollama(model="llama3")

# ----- PROMPTS -----
prompt_essay = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with exactly 100 words."
)

prompt_poem = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} for a 5 year old child with 100 words."
)

# ----- ROUTES -----

# ✅ General Chat Route (Raw LLaMA)
add_routes(app, llm, path="/chat")

# ✅ Essay Generator using LLaMA
add_routes(
    app,
    prompt_essay | llm,
    path="/essay"
)

# ✅ Poem Generator using LLaMA
add_routes(
    app,
    prompt_poem | llm,
    path="/poem"
)

# ----- MAIN -----
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
