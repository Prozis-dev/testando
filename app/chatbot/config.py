import os
from dotenv import load_dotenv

# Guarda variáveis globais

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(dotenv_path=ENV_PATH)

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")
AWS_REGION = os.getenv("AWS_REGION")
AWS_BUCKET = os.getenv("AWS_BUCKET")

DATASET_PATH = "juridicos/"
CHROMA_PATH = "./vector_store/chroma/"

# Grupo de logs
LOG_GROUP = 'ChatbotJuridicoCompass'
# Stream de logs
LOG_STREAM = 'RespostasBedrock'

# Modelos do Bedrock
BEDROCK_MODEL_ID = "amazon.titan-embed-text-v2:0"
LLM_MODEL_ID = "" # Tenho que solicitar o acesso ao Modelo LLM no AWS BedRock para texto
