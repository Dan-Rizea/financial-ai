"""Embed PDFs into Chroma Vectoral DB from documents folder"""
import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

api_key = os.getenv('FinancialAIKey')

# Embed and store the texts
# Supplying a persist_directory will store the embeddings on disk
PERSIST_DIRECTORY = 'db'

embedding = OpenAIEmbeddings(openai_api_key=api_key)
vector_db = Chroma(persist_directory=PERSIST_DIRECTORY,
                embedding_function=embedding)

# To cleanup, you can delete the collection
vector_db.delete_collection()
vector_db.persist()
