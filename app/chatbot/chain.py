from langchain.chains import RetrievalQA
from langchain_community.llms import Bedrock
from vectorstore import load_vector_store
from config import BEDROCK_MODEL_ID

'''
Construir o RetrievalQA chain do chatbot
Conecta o modelo AWS Bedrock ao Chroma
'''

def get_qa_chain(bedrock_client):
    vector_store = load_vector_store()
    llm = Bedrock(model_id=BEDROCK_MODEL_ID, client=bedrock_client)
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )
