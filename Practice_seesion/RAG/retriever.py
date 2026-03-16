import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

DOCUMENTS = [
    "Company leave policy allows 20 days annual leave.",
    "Office holidays are declared annually.",
    "Employees receive health insurance benefits.",
    "Salary information is confidential and managed by HR."
]

# Encode documents
doc_embeddings = model.encode(DOCUMENTS)
dimension = doc_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))

def retrieve(query, top_k=2):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    
    retrieved_docs = [DOCUMENTS[i] for i in indices[0]]
    return " ".join(retrieved_docs)
