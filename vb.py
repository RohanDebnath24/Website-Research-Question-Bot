import pandas as pd
pd.set_option('display.max_colwidth',100)
df=pd.read_csv("sample_text.csv")
#print(df.shape)
print(df)
from sentence_transformers import SentenceTransformer
encoder=SentenceTransformer("all-mpnet-base-v2")
vectors=encoder.encode(df.text)
dim=vectors.shape[1]
print(dim)
import faiss
index = faiss.IndexFlatL2(dim)#created an empty vector index of the specified shape 
print(index)
index.add(vectors)
search_query = "I want to buy a polo t-shirt"
# search_query = "looking for places to visit during the holidays"
# search_query = "An apple a day keeps the doctor away"
vec = encoder.encode(search_query)
#print(vec.shape)#this was showing(768,) only but the index.search() expects 2d array.
import numpy as np
svec=np.array(vec).reshape(1,-1)#converting vector into a 2d array
print(svec.shape)
print(index.search(svec,k=2))


