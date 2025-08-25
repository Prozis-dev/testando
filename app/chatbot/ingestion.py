import boto3
import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN, BUCKET_NAME, DATASET_PATH, AWS_REGION 

'''
Buscar os documentos no S3
Carregar os documentos localmente
Fragmentar em chunks prontos para indexação
'''

def download_from_s3():
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN,
        region_name=AWS_REGION,
    )
    os.makedirs(DATASET_PATH, exist_ok=True)
    
    # Baixa somente um arquivo do diretório 'dataset/'
    # s3.download_file(BUCKET_NAME, "dataset/meuarquivo.pdf", f"{DATASET_PATH}/meuarquivo.pdf") # ? trocar o meuarquivo.pdf pelo arquivo a pegar
    
    # Baixa todos os arquivos do diretório 'dataset/'
    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix="dataset/")
    
    for obj in response.get("Contents", []):
        key = obj["Key"]
        if key.endswitch(".pdf"):
            local_path = os.path.join(DATASET_PATH, os.path.basename(key))
            s3.download_file(BUCKET_NAME, key, local_path)
            print(f"Baixado: {key} -> {local_path}")

def load_and_split():
    loader = PyPDFDirectoryLoader(DATASET_PATH)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=10000,
        chunk_overlap=100
    )
    return splitter.split_documents(docs)
