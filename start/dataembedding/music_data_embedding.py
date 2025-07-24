import sys
import os

# Add the project root or relevant parent folder to sys.path before imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Define the absolute path to music_data PDF file
pdf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dataloadingandchunking', 'Music_Industry_RAG_Document.pdf'))

from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
import vertexai
from vertexai.language_models import TextEmbeddingModel
from dataloadingandchunking.music_data import get_chunks_documents

key_path = "vertexai.json"

credentials = Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

if credentials.expired:
    credentials.refresh(Request())

PROJECT_ID = "agentic-ai-engineering-466919"
REGION = "us-central1"

vertexai.init(project=PROJECT_ID, location=REGION, credentials=credentials)

embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-005")


list_of_chunks_to_embed = get_chunks_documents(pdf_path)

texts = [doc.page_content if hasattr(doc, 'page_content') else str(doc) for doc in list_of_chunks_to_embed]

embeddings = embedding_model.get_embeddings(texts)

#print(embeddings)
