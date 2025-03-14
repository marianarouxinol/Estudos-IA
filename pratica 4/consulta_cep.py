import requests

def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        if "erro" in dados:
            return "CEP não encontrado."
        return f"""
        CEP: {dados['cep']}
        LOGRADOURO: {dados['logradouro']}
        BAIRRO: {dados['bairro']}
        CIDADE: {dados['localidade']}
        ESTADO: {dados['estado']}
        """
    except requests.RequestException as e:
        return f"Erro na consulta: {e}"
def main():
    cep = input("Digite um CEP valido (somente números): ")
    print("Consultando CEP .........")
    resultado = consulta_cep(cep)
    print(resultado)
if __name__ == "__main__":
   main()