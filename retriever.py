from langchain_chroma import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings

DB_PATH = "chroma_db"

embeddings = FastEmbedEmbeddings()

vectorstore = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

def retrieve(query):
    docs = vectorstore.similarity_search(query, k=3)
    return docs