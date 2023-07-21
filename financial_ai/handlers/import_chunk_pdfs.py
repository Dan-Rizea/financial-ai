"""Used in creating embeddings for the CAEN module"""
import os
import textract
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from transformers import GPT2TokenizerFast

api_key = os.getenv('FinancialAIKey')

# Advanced method - Split by chunk

# Convert PDF to text
doc = textract.process("C:\\Users\\Dan\\source\\repos\\financial-ai-1\\Classified_CAEN_v2.pdf")

# Save to .txt and reopen (helps prevent issues)
with open('Classified_CAEN_PDF.txt', 'w', encoding="utf-8") as f:
    f.write(doc.decode('utf-8'))

with open('Classified_CAEN_PDF.txt', 'r', encoding="utf-8") as f:
    text = f.read()

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

chunks = text_splitter.create_documents([text])

# Get embedding model
embeddings = OpenAIEmbeddings(openai_api_key=api_key)

# Create vector database
db = FAISS.from_documents(chunks, embeddings)

QUERY = "Vreau sa imi deschid un salon de tatuaje. Care este codul CAEN pentru aceasta activitate si ce alte activitati ar putea sa coincida cu acelasi cod CAEN?"
docs = db.similarity_search(QUERY)
print(docs[0])

chain = load_qa_chain(OpenAI(openai_api_key=api_key,temperature=0), chain_type="stuff")

docs = db.similarity_search(QUERY)
for doc in docs:
    print(doc)

print(chain.run(input_documents=docs, question=QUERY))
