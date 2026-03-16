from access_control import access_control
from retriever import retrieve
from llm import call_llm
from validation import validate_json, hallucination_check
from logger_config import logger

def rag_pipeline(query, role):

    logger.info(f"Incoming query: {query} | Role: {role}")

    # 1️⃣ RBAC
    allowed, message = access_control(query, role)
    if not allowed:
        logger.warning("Access denied")
        return {"error": message}

    # 2️⃣ Retrieval
    context = retrieve(query)
    logger.info("Documents retrieved")

    # 3️⃣ LLM Call
    response_text = call_llm(context, query)
    logger.info("LLM response received")

    # 4️⃣ JSON Validation
    valid, parsed = validate_json(response_text)
    if not valid:
        logger.error("Invalid JSON format")
        return {"error": "Invalid JSON output"}

    # 5️⃣ Hallucination Check
    if not hallucination_check(parsed["answer"], context):
        logger.error("Hallucination detected")
        return {"error": "Hallucinated response rejected"}

    logger.info("Response validated successfully")
    return parsed
