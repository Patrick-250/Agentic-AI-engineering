from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_chunks_documents(pdf_path="Music_Industry_RAG_Document.pdf"):
    # Load RAG document
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    # Split the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_documents(docs)

# Test it
#chunks = get_chunks_documents()
#print(chunks[0].page_content)   # Print first chunk's text
#print(len(chunks))              # Print total number of chunks



