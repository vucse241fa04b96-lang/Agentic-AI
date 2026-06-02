#embeddings Text
#pip install sentence-transformers


from sentence_transformers import SentenceTransformer

#load the model
model = SentenceTransformer('all-MiniLM-L6-v2')


input_text=[
    "I love programming in Python.",
    "Python is a great language for data science.", 
    "I enjoy machine learning and artificial intelligence."
]

#convert the input text to embeddings
embeddings = model.encode(input_text)
print("Embeddings shape:", embeddings.shape)
print(embeddings)
# pip install scikit-learn
from sklearn.metrics.pairwise import cosine_similarity

similarity_data=cosine_similarity(
    [embeddings[0]],  #Query embedding(first sentence)
    embeddings[1:]    #compare the rest of the embedding
)
print("Similarity Scores:",similarity_data)



#1.load the text data from a file
#2.Convert the text data to Tokenizer
#3.Model Training(Generate Embeddings) Vector Database
#4.Vector stored in database(Mongodb,Postgres,Pinecone,weaviate,etc.)
#5.Similarity Search