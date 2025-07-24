from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

#load my RAG document music data
loader=PyPDFLoader("Music_Industry_RAG_Document.pdf")
docs=loader.load()

#with recursive, now i can split the text by characters


text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks_documents = text_splitter.split_documents(docs)

#print(chunks_documents[0])
#print(len(chunks_documents))

