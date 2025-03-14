import requests

def obter_cotacao(moeda):
    try:
        # url = f'https://economia.awesomeapi.com.br/json/last/{moeda}-BRL'
        # url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{moeda}-BRL"
        url = f'https://brapi.dev/docs/moedas/available{moeda}-BRL'
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  # Levanta um erro se a resposta for inválida (ex: 404, 500)
        return resposta.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter a cotação: {e}")
        return None

def exibir_cotacao(cotacao, moeda):
    try:
        par_moeda = f'{moeda}BRL'
        dados = cotacao[par_moeda]

        print(f"\nCotação {dados['name']}:")
        print(f"Valor atual (compra): R$ {dados['bid']}")
        print(f"Valor atual (venda): R$ {dados['ask']}")
        print(f"Máximo do dia: R$ {dados['high']}")
        print(f"Mínimo do dia: R$ {dados['low']}")
        print(f"Data e hora da última atualização: {dados['create_date']}\n")

    except KeyError:
        print("Não foi possível encontrar a cotação para essa moeda.")

def main():
    while True:
        try:
            moeda = input("Digite o código da moeda desejada (ex: USD, EUR, GBP) ou 'sair' para encerrar: ").upper()
            if moeda == 'SAIR':
                print("Encerrando o programa...")
                break
            if not moeda.isalpha():
                raise ValueError("Código inválido. Digite apenas letras.")

            cotacao = obter_cotacao(moeda)
            if cotacao:
                exibir_cotacao(cotacao, moeda)
            else:
                print("Não foi possível obter a cotação. Tente novamente mais tarde.")

        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()