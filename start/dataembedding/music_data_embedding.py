from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
import vertexai
from vertexai.language_models import TextEmbeddingModel




key_path="vertexai.json"

Credentials=Credentials.from_service_account_file(

  key_path,
  scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

if Credentials.expired:
  Credentials.refresh(Request())

PROJECT_ID="agentic-ai-engineering-466919"
REGION="us-central1"


#start of vertex ai initialization

vertexai.init(project=PROJECT_ID,location=REGION,credentials=Credentials)

embedding_model=TextEmbeddingModel.from_pretrained("text-embedding-005")
sentence_to_embed="this would start the embedding of music data "
embedding=embedding_model.get_embeddings([sentence_to_embed])
#print(embedding)
