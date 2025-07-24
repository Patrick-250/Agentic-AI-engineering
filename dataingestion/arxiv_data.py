from langchain_community.document_loaders import ArxivLoader
loader=ArxivLoader(query="1706.03762",load_max_docs=2) #load attention is all you need paper with its parameter on arxiv
docs=loader.load()
# print(docs)

