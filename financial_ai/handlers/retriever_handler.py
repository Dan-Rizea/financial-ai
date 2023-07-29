"""Used in creating embeddings for the CAEN module"""
import os
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate

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

    # Build a template
    prompt_template = """You will receive Romanian document fragments that contain economic activity information alongside their respective CAEN codes///
A user can ask for either a CAEN code which has to be a number |||0000, 000, 00||| or a letter |||F - Constructii, H - Transport și depozitare|||///
The corresponding CAEN code or identifying letter will always be behind the economic activity's name |||011 Cultivarea plantelor nepermanente|||
Your task is to provide the user with the correct information in regards to their prompts and always answer in Romanian///
If the provided documents do not match the user's input or if the question is too ambiguous tell the user to be more specific///
If more than one code could match the prompt tell the user that there are many CAEN codes that could match and that he has to be more specific///

Document contents:
|||
{context}
|||

Prompt:'''{question}'''
"""

    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    chain_type_kwargs = {"prompt": PROMPT}

    # create the chain to answer questions
    qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=api_key),
                                            chain_type="stuff",
                                            retriever=retriever,
                                            return_source_documents=True,
                                            chain_type_kwargs=chain_type_kwargs)

    # Cite sources
    def process_llm_response(llm_response):
        print(prompt)
        print(llm_response['result'])
        print('\nSources:')
        for source in llm_response["source_documents"]:
            print(source.metadata['source'])
            print(source.page_content)

    llm_response = qa_chain(prompt)
    process_llm_response(llm_response)

    return llm_response['result']
