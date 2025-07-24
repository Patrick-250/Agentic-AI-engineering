
from langchain_community.document_loaders import JSONLoader
from langchain_text_splitters import RecursiveJsonSplitter
import json
loader=JSONLoader(file_path="app_data.json",text_content=False ,jq_schema=".")
docs=loader.load()
#print(docs)
raw_json=json.loads(docs[0].page_content)
json_splitter=RecursiveJsonSplitter(max_chunk_size=100)
json_chunks=json_splitter.split_json(raw_json)
#print(json_chunks[0])