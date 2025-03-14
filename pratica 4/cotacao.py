import requests
from datetime import datetime

def cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-brl"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        cotacao = dados.get(f"{moeda}BRL")
        if not cotacao:
            return
        valor = float(cotacao['bid'])
        maximo = float(cotacao['high'])
        minima = float(cotacao['low'])
        data_hora = datetime.fromtimestamp(int(cotacao['timestamp']))
        return f"""
        Moeda: {moeda} para BRL
        Valor atual: R$ {valor:.4f}
        Máxima do dia: R$ {maximo:.4f}
        Minima do dia: R$ {minima:.4f}
        Data/Hora da cotação: {data_hora.strftime('%d/%m/%Y %H:%M:%S')}
        """
    except requests.RequestException as e:
        return f"Erro ao obter cotação: {e}"
    except KeyError:
        return "Moeda não encontrada ou não suportada."

def main():
    """Função principal para solicitar uma moeda ao usuário e exibir sua cotação."""
    moeda = input("Digite o código da moeda para cotação (ex: USD, EUR, GBP): ").upper()

    print("\nObtendo cotação...")

resultado = obter_cotacao(moeda)
print(resultado)


if __name__ == "__main__":
    main()