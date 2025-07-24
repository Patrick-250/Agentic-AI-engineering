from langchain_community.document_loaders import PyPDFLoader

#load my RAG document music data
loader=PyPDFLoader("Music_Industry_RAG_Document.pdf")
docs=loader.load()
