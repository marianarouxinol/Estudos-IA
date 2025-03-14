import requests

def consultar_cep():
    while True:
        try:
            cep = input("Digite o CEP para consulta (somente números): ")
            if cep.isdigit() and len(cep) == 8:
                break
            else:
                print("O CEP deve conter 8 dígitos. Por favor, tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if response.status_code == 200:
        response.raise_for_status()
        data = response.json()
        print("Endereço encontrado:")
        print(f"Logradouro: {data['logradouro']}")
        print(f"Bairro: {data['bairro']}")
        print(f"Cidade: {data['localidade']}")
        print(f"Estado: {data['uf']}")
    else:
        print("Erro ao acessar a API 'ViaCEP'.")

if __name__ == '__main__':
   consultar_cep()