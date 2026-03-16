# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def call_llm(context, query):
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "Respond only in JSON."},
#             {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
#         ],
#         temperature=0
#     )

#     return response.choices[0].message.content


import random
import json

def call_llm(context, query):
    # Simulated JSON response
    response = {
        "answer": "Company leave policy allows 20 days annual leave.",
        "confidence": round(random.uniform(0.7, 0.95), 2),
        "source_used": True
    }

    return json.dumps(response)
