from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import openai
from dotenv import load_dotenv
import os
import shutil
import sys

# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv()

# Set OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

CHROMA_PATH = "chroma"
DATA_PATH = 'data/books/temp/'

def main():
    generate_data_store()

def generate_data_store():
    documents = load_documents()
    print(documents[0])
    chunks = split_text(documents)
    save_to_chroma(chunks)

def load_documents():
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    return document_loader.load()

def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks

def save_to_chroma(chunks: list[Document]):
    # Check if the Chroma vector store exists
    if os.path.exists(CHROMA_PATH):
        # Load the existing database
        db = Chroma(persist_directory=CHROMA_PATH, embedding_function=OpenAIEmbeddings())
    else:
        # Create a new database if it doesn't exist
        db = Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH)

    # Define the maximum batch size allowed
    max_batch_size = 5460

    # Split the chunks into smaller batches and add them to the database
    for i in range(0, len(chunks), max_batch_size):
        batch = chunks[i:i + max_batch_size]
        db.add_documents(batch)

    # Persist the database with the new chunks included
    db.persist()
    print(f"Saved {len(chunks)} new chunks to {CHROMA_PATH}.")

if __name__ == "__main__":
    main()
