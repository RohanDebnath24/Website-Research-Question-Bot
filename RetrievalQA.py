import os
import streamlit as st
import pickle
import time
import langchain
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate 
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import SeleniumURLLoader

os.environ['OPENAI_API_KEY']="[Place-your-own-api]"
LLM=OpenAI(temperature=0.9,max_tokens=1000)
loaders = SeleniumURLLoader(urls=[
    "https://www.moneycontrol.com/news/business/markets/wall-street-rises-as-tesla-soars-on-ai-optimism-11351111.html",
    "https://www.moneycontrol.com/news/business/tata-motors-launches-punch-icng-price-starts-at-rs-7-1-lakh-11098751.html"
])
data=loaders.load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

# As data is of type documents we can directly use split_documents over split_text in order to get the chunks.
docs = text_splitter.split_documents(data)
embeddings=OpenAIEmbeddings()
vectorindex_openai=FAISS.from_documents(docs,embeddings)
#storing vector index create in local
file_path="vector_index.pkl"
with open(file_path,"wb") as f:
    pickle.dump(vectorindex_openai,f)
if os.path.exists(file_path):
    with open(file_path,"rb") as f:
        vectorindex = pickle.load(f)
chain=RetrievalQAWithSourcesChain.from_llm(llm=LLM,retriever=vectorindex.as_retriever())
query="What is the price of Tiago ICNG"
langchain.debug=True
chain({"question":query},return_only_outputs=True)
