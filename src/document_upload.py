from PyPDF2 import PdfReader
from src.logger import logging
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from firebase_admin import firestore
from pinecone import Pinecone, ServerlessSpec
from src.exception import CustomException
from dotenv import load_dotenv
from firebase_admin import credentials, initialize_app, firestore
import sys
import os


load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "ragmodel-91184-firebase-adminsdk-mn1rb-1729150ab9.json"
cred = credentials.Certificate(os.environ["FIRE_BASE"])
initialize_app(cred)

# for initializing Pinecone
pc = Pinecone(
    api_key=os.environ["PINCONE_API"]
)

index_name = 'langchainvector'

# for checking the index exits or not
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=768,
        metric='cosine',
        spec=ServerlessSpec(cloud='aws', region='us-east-1')
    )

def handle_document_upload(uploaded_file, chat_name):
    try:
        text = extract_pdf_text(uploaded_file)
        text_chunks = split_text_into_chunks(text)

        # for Ccreating  Pinecone Index
        index = pc.Index(index_name)
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vectors = embeddings.embed_documents(text_chunks)

        upsert_data = [
            {"id": f"{chat_name}_{i}", "values": vector, "metadata": {"text": text_chunks[i]}}
            for i, vector in enumerate(vectors)
        ]

        # Upsert vectors to Pinecone
        index.upsert(vectors=upsert_data,namespace=chat_name)

        # Store index metadata in Firestore
        db = firestore.client()
        db.collection("document_indices").document(chat_name).set({"index_name": index_name})

        logging.info(f"Document {chat_name} indexed successfully")

    except Exception as e:
        logging.error(f"Error during document upload: {str(e)}")
        raise CustomException(e, sys)

#  to extract text from PDF
def extract_pdf_text(pdf_file):
    text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# to split text into chunks
def split_text_into_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    return text_splitter.split_text(text)
