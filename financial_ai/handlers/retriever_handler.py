"""Used in creating embeddings for the CAEN module"""
import os
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

api_key = os.getenv('FinancialAIKey')

async def retrieve_embedded_data(prompt):
    """Embed a PDF and search through it using ChatGPT"""

    embedding = OpenAIEmbeddings(openai_api_key=api_key)
    persist_directory = 'db'

    vectordb = Chroma(persist_directory=persist_directory, 
                      embedding_function=embedding)

    retriever = vectordb.as_retriever()
    docs = retriever.get_relevant_documents(prompt)
    len(docs)
    retriever = vectordb.as_retriever(search_kwargs={"k": 2})

    # create the chain to answer questions 
    qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=api_key),
                                            chain_type="stuff", 
                                            retriever=retriever, 
                                            return_source_documents=True)
    
    ## Cite sources
    def process_llm_response(llm_response):
        print(llm_response['result'])
        print('\n\nSources:')
        for source in llm_response["source_documents"]:
            print(source.metadata['source'])

    llm_response = qa_chain(prompt)
    process_llm_response(llm_response)

    return llm_response['result']
