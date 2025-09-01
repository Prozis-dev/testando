import boto3
import datetime
from botocore.exceptions import ClientError
from config import AWS_REGION, LOG_GROUP, LOG_STREAM

# Inicializa o cliente do CloudWatch uma vez para reutilização
try:
    logs_client = boto3.client('logs', region_name=AWS_REGION)
except Exception as e:
    print(f"Erro ao inicializar o cliente Boto3 para CloudWatch: {e}")
    logs_client = None

def _ensure_log_group_and_stream_exist():
    # Garante que o grupo e o stream de logs existam no CloudWatch
    if not logs_client:
        return

    try:
        logs_client.create_log_group(logGroupName=LOG_GROUP)
    except ClientError as e:
        if e.response['Error']['Code'] != 'ResourceAlreadyExistsException':
            print(f"Erro ao criar Log Group: {e}")

    try:
        logs_client.create_log_stream(logGroupName=LOG_GROUP, logStreamName=LOG_STREAM)
    except ClientError as e:
        if e.response['Error']['Code'] != 'ResourceAlreadyExistsException':
            print(f"Erro ao criar Log Stream: {e}")

def log_interaction(question: str, answer: str):
    # Registra a pergunta e a resposta do chatbot no Amazon CloudWatch

    if not logs_client:
        print("Logging desabilitado pois o cliente do CloudWatch não foi inicializado.")
        return

    _ensure_log_group_and_stream_exist()

    timestamp = int(datetime.datetime.now().timestamp() * 1000)
    log_message = f"[PERGUNTA]: {question}\n[RESPOSTA]: {answer}"

    try:
        logs_client.put_log_events(
            logGroupName=LOG_GROUP,
            logStreamName=LOG_STREAM,
            logEvents=[
                {
                    'timestamp': timestamp,
                    'message': log_message
                }
            ]
        )
        print("Log enviado com sucesso para o CloudWatch.")
    except Exception as e:
        print(f"Erro ao enviar log para o CloudWatch: {e}")