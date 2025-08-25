import streamlit as st
import boto3
from ingestion import download_from_s3, load_and_split
from vectorstore import build_vector_store
from chain import get_qa_chain

# Interface principal

st.title("Chatbot RAG com LangChain + Bedrock")

if st.button("Atualizar Base"):
    download_from_s3()
    docs = load_and_split()
    build_vector_store(docs)
    st.success("Base atualizada!")

query = st.text_input("Digite sua pergunta:")

if query:
    client = boto3.client("bedrock-runtime")
    qa = get_qa_chain(client)
    result = qa({"query": query})
    st.write("**Resposta:**", result["result"])
