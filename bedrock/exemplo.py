# Usar a API de conversação para enviar a mensagem - Amazon Titan Text.

import boto3  # Biblioteca SDK da AWS para interagir com serviços da AWS, incluindo o Amazon Bedrock
from botocore.exceptions import ClientError  # Importa a exceção para tratar erros da AWS

# Criar o cliente do Bedrock Runtime na região us-east-1
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Definir o modelo da Amazon Titan a ser utilizado
model_id = "amazon.titan-text-express-v1"

# Definir a mensagem do usuário para iniciar o diálogo
user_message = "voce consegue me falar quais os resultados dos jogos de futebol do mundial da fifa 2022? "

# Estruturar a conversa como uma lista de mensagens
conversation = [
    {
        "role": "user",  # Define o emissor da mensagem como o usuário
        "content": [{"text": user_message}],  # Conteúdo da mensagem enviada
    }
]

try:
    # Enviar a mensagem para o modelo Titan através da API do Bedrock
    response = client.converse(
        modelId=model_id,  # Define o modelo a ser utilizado
        messages=conversation,  # Envia a mensagem na estrutura esperada
        inferenceConfig={  # Configurações da inferência
            "maxTokens": 800,  # Define o limite de tokens na resposta gerada
            "temperature": 0.5,  # Controla o grau de aleatoriedade da resposta
            "topP": 0.9  # Define a probabilidade acumulada para limitar palavras menos prováveis
        },
    )

    # Extrair e exibir a resposta gerada pelo modelo
    response_text = response["output"]["message"]["content"][0]["text"]  # Acessa a resposta gerada dentro da estrutura JSON retornada pela API
    print(response_text)  # Exibe a resposta gerada pelo modelo

except (ClientError, Exception) as e:  # Captura erros da AWS ou erros gerais
    print(f"ERRO: Falha na chamada '{model_id}'. Erro: {e}")  # Exibe a mensagem de erro
    exit(1)  # Encerra a execução do programa em caso de erro