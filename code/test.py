import requests
import json

# Verificar se as iniciativas estão acessíveis
url_listagem_iniciativas = "http://localhost:3000/initiatives"
response_listagem = requests.get(url_listagem_iniciativas)

if response_listagem.status_code == 200:
    # Iniciativas acessíveis, criar uma nova iniciativa
    url_criar_iniciativa = "http://localhost:3000/initiatives"
    criar_iniciativa = {
        "name": "Criação de Website de Vendas",
        "status": "PENDING",
        "description": "Este website será criado para aumentar as vendas da empresa.",
        "observation": "Utilizar FastAPI para criar a API do website.",
        "company_id": 42,
        "module_id": 28
    }

    # Serializar o dicionário como JSON
    dados_json = json.dumps(criar_iniciativa)

    # Enviar como dados usando o parâmetro data
    response_criacao = requests.post(url_criar_iniciativa, data=dados_json, headers={'Content-Type': 'application/json'})

    # Verificar se a iniciativa foi criada com sucesso
    if response_criacao.status_code == 200:
        print("Teste Passou: Iniciativa criada com sucesso!")

        # Analisar a resposta JSON da criação para obter o ID da iniciativa criada
        nova_iniciativa = response_criacao.json()
        nova_iniciativa_id = int(nova_iniciativa.get("id"))
        print("Id da nova iniciativa:", nova_iniciativa_id)

        # Verificar se o ID da nova iniciativa está na lista de iniciativas
        url_listagem_iniciativas = "http://localhost:3000/initiatives"
        response_listagem = requests.get(url_listagem_iniciativas)

        if response_listagem.status_code == 200:
            print("Teste Passou: Iniciativas acessíveis após a nova inserção. Listando Ids das iniciativas:")
            lista_iniciativas = response_listagem.json().get("data")
            print([iniciativa["id"] for iniciativa in lista_iniciativas])

            if nova_iniciativa_id in [iniciativa["id"] for iniciativa in lista_iniciativas]:
                print("Teste Passou: O ID da nova iniciativa aparece na lista de iniciativas! Teste finalizado com sucesso!")
            else:
                print("Teste Falhou: O ID da nova iniciativa não aparece na lista de iniciativas.")
        else:
            print("Teste Falhou: Iniciativas indisponíveis após a nova inserção.")
    else:
        print("Teste Falhou: Falha ao criar a iniciativa.")
else:
    print("Teste Falhou: Iniciativas indisponíveis.")
