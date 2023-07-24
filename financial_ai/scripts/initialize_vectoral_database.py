"""Embed PDFs into Chroma Vectoral DB from documents folder"""
import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import GPT2TokenizerFast
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import DirectoryLoader
from langchain.vectorstores import Chroma

api_key = os.getenv('FinancialAIKey')

loader = DirectoryLoader('C:/Users/Dan/source/repos/financial-ai-1/documents/', glob="./*.pdf", loader_cls=PyPDFLoader)
documents = loader.load()

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
def count_tokens(text: str) -> int:
    """Create function to count tokens"""
    return len(tokenizer.encode(text))

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 512,
    chunk_overlap  = 24,
    length_function = count_tokens,
)
texts = text_splitter.split_documents(documents)

# Embed and store the texts
# Supplying a persist_directory will store the embeddings on disk
persist_directory = 'db'

embedding = OpenAIEmbeddings(openai_api_key=api_key)
vectordb = Chroma.from_documents(documents=texts, 
                                embedding=embedding,
                                persist_directory=persist_directory)

vectordb.persist()
vectordb = None

vectordb = Chroma(persist_directory=persist_directory, 
                embedding_function=embedding)

