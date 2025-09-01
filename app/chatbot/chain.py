import boto3
from langchain.chains import RetrievalQA
from langchain_community.llms import Bedrock
from vectorstore import load_vector_store
from config import AWS_REGION, LLM_MODEL_ID
from aws_logging import log_interaction # Função de log

'''
Construir o RetrievalQA chain e a função principal do chatbot
Conecta o modelo AWS Bedrock ao ChromaDB e integra o logging
'''

def get_qa_chain(bedrock_client):
    # Cria e retorna a chain RetrievalQA
    vector_store = load_vector_store()
    llm = Bedrock(model_id=LLM_MODEL_ID, client=bedrock_client)

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )

def get_chatbot_answer(query: str) -> dict:
    """
    Função principal para obter a resposta do chatbot
    Função que a API (Pessoa 4) deve chamar
    """
    try:
        # Inicializa o cliente Bedrock
        bedrock_client = boto3.client("bedrock-runtime", region_name=AWS_REGION)

        # Obtém a chain de QA
        qa_chain = get_qa_chain(bedrock_client)

        # Executa a consulta
        result = qa_chain.invoke({"query": query})

        answer = result.get("result", "Desculpe, não consegui encontrar uma resposta.")

        # LOGGING
        # Envia a pergunta e a resposta para o CloudWatch
        log_interaction(question=query, answer=answer)

        # Extrai os documentos fonte para referência (opcional)
        source_docs = result.get("source_documents", [])
        source_pages = [doc.metadata.get('page', '?') for doc in source_docs]

        return {
            "answer": answer,
            "source_pages": source_pages
        }

    except Exception as e:
        error_message = f"Ocorreu um erro no processamento da chain: {e}"
        print(error_message)
        # Loga o erro também, se desejar
        log_interaction(question=query, answer=f"ERRO: {error_message}")
        return {"answer": "Ocorreu um erro ao processar sua pergunta."}