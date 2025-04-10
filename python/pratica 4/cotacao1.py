import requests

def obter_cotacao(moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}-BRL'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None

def exibir_cotacao(cotacao, moeda):
    par_moeda = f'{moeda}BRL'
    if par_moeda in cotacao:
        dados = cotacao[par_moeda]
        print(f"\nCotação {dados['name']}:")
        print(f"Valor atual (compra): R$ {dados['bid']}")
        print(f"Valor atual (venda): R$ {dados['ask']}")
        print(f"Máximo do dia: R$ {dados['high']}")
        print(f"Mínimo do dia: R$ {dados['low']}")
        print(f"Data e hora da última atualização: {dados['create_date']}")
    else:
        print("Não foi possível obter a cotação para a moeda informada.")

def main():
    moeda = input("Digite o código da moeda desejada (ex: USD, EUR, GBP): ").upper()
    cotacao = obter_cotacao(moeda)
    if cotacao:
        exibir_cotacao(cotacao, moeda)
    else:
        print("Erro ao consultar a cotação. Verifique o código da moeda e tente novamente.")

if __name__ == "__main__":
    main()