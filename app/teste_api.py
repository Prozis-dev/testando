import requests

URL = "https://fg92smazfe.execute-api.sa-east-1.amazonaws.com/dev/ask"

HEADERS = {
    #"x-api-key": "CHAVE_API",   
    "Content-Type": "application/json"
}

payload = {"pergunta": "Teste de integração"}

response = requests.post(URL, json=payload, headers=HEADERS)
print("Status code:", response.status_code)
print("Resposta:", response.text)

# Para rodar o teste da API via terminal, use:
    # python app/teste_api.py
    # Se tudo tiver funcionando, você verá algo como:
        # Status code: 200
        # Resposta JSON: {'resposta': 'Em breve'}
