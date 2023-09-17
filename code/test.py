import requests

# Verificar se as iniciativas estão acessíveis
url = "localhost:3000/initiatives"
response = requests.get(url)

if response.status_code == 200:
    # Iniciativas acessíveis, criar uma nova iniciativa
    url_criar_iniciativa = "localhost:3000/initiatives"
    criar_iniciativa = {
    "name": "testeIsrael",
    "status": "PENDING",
    "description": "testeIsrael",
    "observation": "testeIsrael",
    "company_id": 42,
    "module_id": 28
    }
    response = requests.post(url_criar_iniciativa, data=criar_iniciativa)

    # Verificar se a iniciativa foi criada com sucesso
    if response.status_code == 200:
        print("Teste Passou: Iniciativa criada com sucesso!")
    else:
        print("Teste Falhou: Falha ao criar a iniciativa.")
else:
    print("Teste Falhou: Iniciativas indisponíveis.")
