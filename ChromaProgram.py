#pip install chromadb
import chromadb
from groq import Groq
import os

client=Groq(api_key="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")

#create a chromadb client
Clientdbs=chromadb.PersistentClient(path="./chroma_dbs")
#create a collection
collection=Clientdbs.get_or_create_collection(name="my_collection")
#add data to the collection
collection.add(
    documents=["Python with AI Improves Productivity",
               "ML, Dim Predicts the disease",
               "AI in Healthcare: Revolutionizing Patient Care"],
    ids=["doc1","doc2","doc3"],
    metadatas=[{"source":"source1"},
               {"source":"source2"},
               {"source":"source3"}]
)

#query the collection
query="How is AI used in healthcare?"
results=collection.query(
    query_texts=[query],
    n_results=2
)
print("Query Results:")

Context="/n".join(results["documents"][0])
print(Context)
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
print("LLM Response:")
print(response.choices[0].message.content)
