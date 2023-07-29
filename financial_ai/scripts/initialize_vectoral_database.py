"""Embed PDFs into Chroma Vectoral DB from documents folder"""
import os
from transformers import GPT2TokenizerFast
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain.vectorstores import Chroma

api_key = os.getenv('FinancialAIKey')

# loader = DirectoryLoader('C:/Users/Dan/source/repos/financial-ai-1/pdf_documents/', glob="./*.pdf", loader_cls=PyPDFLoader)
# documents = loader.load()

loader = DirectoryLoader('C:/Users/Dan/source/repos/financial-ai-1/txt_documents/', glob="./*.txt", loader_cls=TextLoader)
documents = loader.load()

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
def count_tokens(text: str) -> int:
    """Create function to count tokens"""
    return len(tokenizer.encode(text))

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 1024,
    chunk_overlap  = 96,
    length_function = count_tokens,
)
texts = text_splitter.split_documents(documents)

# Embed and store the texts
# Supplying a persist_directory will store the embeddings on disk
PERSIST_DIRECTORY = 'db'

embedding = OpenAIEmbeddings(openai_api_key=api_key)
vector_db = Chroma.from_documents(documents=texts,
                                embedding=embedding,
                                persist_directory=PERSIST_DIRECTORY)

vector_db.persist()

vector_db = None
vector_db = Chroma(persist_directory=PERSIST_DIRECTORY,
                embedding_function=embedding)
