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
BUCKET_NAME = os.getenv("AWS_BUCKET")
DATASET_PATH = "./dataset"
CHROMA_PATH = "./vector_store/chroma/"

print("DEBUG REGION:", AWS_REGION)
print("DEBUG BUCKET:", BUCKET_NAME)
print("DEBUG BASE_DIR:", BASE_DIR)

# Modelos do Bedrock
BEDROCK_MODEL_ID = "anthropic.claude-v2"
