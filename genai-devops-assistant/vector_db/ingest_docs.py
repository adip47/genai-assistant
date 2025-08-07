from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def ingest_to_faiss(doc_path: str, index_path: str = "faiss_index"):
    loader = TextLoader(doc_path)
    documents = loader.load()

    # Split the documents into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    # Embed the chunks using OpenAI
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(chunks, embeddings)

    # Save index to disk
    vectordb.save_local(index_path)
    print(f"Documents ingested to FAISS index at: {index_path}")

if __name__ == "__main__":
    DOC_PATH = "sample_docs/devops_notes.txt"  # Change path to your doc
    ingest_to_faiss(DOC_PATH)
