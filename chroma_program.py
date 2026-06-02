
# RAG Application using Ollama + ChromaDB
# Model : llama3.2


# Install Packages:
# pip install ollama
# pip install chromadb
# pip install sentence-transformers

import chromadb
import ollama
from sentence_transformers import SentenceTransformer

# STEP 1 : CREATE VECTOR DATABASE
# Create ChromaDB persistent client
client = chromadb.PersistentClient(path="./chroma_db")

# Create collection
collection = client.get_or_create_collection(
    name="ai_knowledge"
)


# STEP 2 : DOCUMENTS
documents = [
    "Artificial Intelligence improves healthcare diagnosis.",
    "Machine Learning helps detect diseases early.",
    "Natural Language Processing is used in chatbots.",
    "AI in education personalizes student learning.",
    "Deep Learning is widely used in computer vision."
]

ids = ["doc1", "doc2", "doc3", "doc4", "doc5"]


# STEP 3 : LOAD EMBEDDING MODEL
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Generate embeddings
embeddings = embedding_model.encode(documents)


# STEP 4 : STORE DATA IN CHROMADB
try:
    collection.delete(ids=ids)
except:
    pass

collection.add(
    documents=documents,
    embeddings=embeddings.tolist(),
    ids=ids
)

print("Documents stored successfully!")


# STEP 5 : USER QUERY LOOP
while True:

    query = input("\nEnter your query: ")

    if query.lower() == "exit":
        print("Exiting program...")
        break

  
    # STEP 6 : CREATE QUERY EMBEDDING
    query_embedding = embedding_model.encode([query])

  
    # STEP 7 : SEMANTIC SEARCH
    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=2
    )

    # Retrieved context
    context = "\n".join(results["documents"][0])

    print("\nRetrieved Context:\n")
    print(context)

  
    # STEP 8 : SEND CONTEXT TO OLLAMA
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": f"""
Use the following context to answer the user question.

Context:
{context}
"""
            },
            {
                "role": "user",
                "content": query
            }
        ]
    )

  
    # STEP 9 : PRINT RESPONSE
    print("\nAI Response:\n")
    print(response["message"]["content"])
