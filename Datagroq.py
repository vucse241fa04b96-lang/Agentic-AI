import os
from groq import Groq
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Set API Key
api_key = "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"

client = Groq(api_key=api_key)

# Documents
Text_docs = [
    "AI Healthcare System",
    "AI in Education",
    "AI in Finance",
    "NLP in Healthcare",
    "NLP in Education"
]

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings
Doc_embeddings = model.encode(Text_docs)

print("Embeddings shape:", Doc_embeddings.shape)

# Create FAISS index
D = Doc_embeddings.shape[1]

index = faiss.IndexFlatL2(D)

index.add(np.array(Doc_embeddings))

# User Query
query = "How is AI used in healthcare?"

query_embedding = model.encode([query])

# Search similar docs
dists, ids = index.search(np.array(query_embedding), k=2)

# Retrieve context
Context = ""

for idx in ids[0]:
    Context += Text_docs[idx] + "\n"

print("Context:\n", Context)

# LLM Response
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": f"""
Use this context to answer the user query:

{Context}
"""
        },
        {
            "role": "user",
            "content": query
        }
    ]
)

print("\nAI Response:\n")

print(response.choices[0].message.content)