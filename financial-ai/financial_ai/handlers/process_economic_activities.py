"""Module required to get the OpenAI API Key from env vars"""
import os
from langchain.llms import OpenAI

api_key = os.getenv('FinancialAIKey')

async def print_test():
    """This is a test method. Will delete later"""    
    llm = OpenAI(openai_api_key=api_key,temperature=0)
    output = llm("Care este codul CAEN pentru activitatea de pescuit maritim?")
    print(output)

async def get_economic_category(intrebare):
    """This method is meant to query an economic activity through OpenAI"""    
    template=f"""
    Avand urmatoarele activitati economice, care ar fi categoria care se potriveste cel mai bine cu intrebarea?
    
    Categorii: Agricultură, silvicultură și pescuit|
    Industria extractivă|
    Industria prelucrătoare| 
    Producția și furnizarea de energie electrică și termică gaze apă caldă și aer condiționat|
    Distribuția apei; salubritate, gestionarea deșeurilor activități de decontaminare|
    Construcții|
    Comerț cu ridicata și cu amănuntul; repararea autovehiculelor și motocicletelor|
    Transport și depozitare|
    Hoteluri și restaurante|
    Informații și comunicații|
    Intermedieri financiare și asigurări|
    Tranzacții imobiliare|
    Activități profesionale, științifice și tehnice|
    Activități de servicii administrative și activități de servicii suport|
    Administrație publică și apărare; asigurări sociale din sistemul public|
    Învățământ|
    Sănătate și asistență socială|
    Activitați de spectacole, culturale și recreative|
    Alte activități de servicii|
    Activități ale gospodăriilor private în calitate de angajator de personal casnic; activități ale gospodăriilor private de producere de bunuri și servicii destinate consumului propriu|
    Activități ale organizațiilor și organismelor extrateritoriale|
    
    Intrebare: {intrebare}
    """

    llm = OpenAI(openai_api_key=api_key,temperature=0)
    output = llm(template)
    print(output)
    return output

    # prompt = PromptTemplate(input_variables=["economicCategoryInquiry"], template=template)
