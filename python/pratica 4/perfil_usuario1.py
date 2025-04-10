import requests

def gerar_perfil():
    # Fazer uma solicitação GET à API 'Random User Generator'
    response = requests.get('https://randomuser.me/api/')
    
    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Processar a resposta JSON
        data = response.json()
        usuario = data['results'][0]
        
        # Extrair informações do usuário
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        # Exibir as informações do usuário
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}")
    else:
        print("Erro ao acessar a API 'Random User Generator'.")

if __name__ == '__main__':
  gerar_perfil()