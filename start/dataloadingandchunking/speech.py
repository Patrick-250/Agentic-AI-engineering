from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

loader=TextLoader("speech.txt",encoding="utf-8")
docs=loader.load()
#print(docs)

text_splitter=CharacterTextSplitter(separator="\n\n",chunk_size=2000,chunk_overlap=400)
chunks=text_splitter.split_documents(docs)



