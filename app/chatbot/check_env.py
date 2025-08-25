import os
import boto3
from dotenv import load_dotenv
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Arquivo para testes do .env

def check_env():
    load_dotenv()

    aws_key = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_token = os.getenv("AWS_SESSION_TOKEN")
    aws_region = os.getenv("AWS_REGION")
    bucket_name = os.getenv("AWS_BUCKET")

    print("=== Verificando variáveis de ambiente ===")
    print(f"AWS_ACCESS_KEY_ID: {aws_key[:4] + '...' if aws_key else 'NÃO DEFINIDO'}")
    print(f"AWS_SECRET_ACCESS_KEY: {aws_secret[:2] + '***' if aws_secret else 'NÃO DEFINIDO'}")
    print(f"AWS_REGION: {aws_region if aws_region else 'NÃO DEFINIDO'}")
    print(f"AWS_BUCKET: {bucket_name if bucket_name else 'NÃO DEFINIDO'}")

    if not aws_key or not aws_secret:
        print("\nCredenciais ausentes no .env. Verifique se você preencheu corretamente.")
        return

    # Testa conexão com S3
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=aws_key,
            aws_secret_access_key=aws_secret,
            aws_session_token=aws_token,
            region_name=aws_region,
        )

        print("\n=== Testando acesso ao S3 ===")
        resp = s3.list_buckets()
        buckets = [b["Name"] for b in resp["Buckets"]]

        print("Buckets encontrados:", buckets)
        if bucket_name and bucket_name not in buckets:
            print(f"O bucket '{bucket_name}' NÃO foi encontrado nessa conta.")
        else:
            print(f"Acesso ao bucket '{bucket_name}' OK!")

    except (NoCredentialsError, PartialCredentialsError):
        print("\nErro: credenciais inválidas ou incompletas.")
    except ClientError as e:
        print(f"\nErro AWS: {e}")

if __name__ == "__main__":
    check_env()