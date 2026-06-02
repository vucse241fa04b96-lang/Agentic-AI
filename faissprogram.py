#Faiss package
#pip install faiss-cpu   --u can use this only
#pip install faiss-cpu


import faiss
import numpy as np

#Data Dimensions
D=64
#Number of vectors
NVectors=10000
#Generate random vectors
np.random.seed(42)
xb=np.random.random((NVectors,D)).astype('float32')
#Create a Faiss index
index=faiss.IndexFlatL2(D)
#Add vectors to the index
index.add(xb)
print(f"Number of vectors in the index:{index.ntotal}")
#Query Vector(Randomly generated)
QVector=np.random.random((1,D)).astype('float32')
#Search for the 5 nearest neighbors
k=5
Dists,Ids=index.search(QVector,k)
print(f"Distances:{Dists}")
print(f"Indices:{Ids}")

