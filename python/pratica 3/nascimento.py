import datetime

def idade_em_dias(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade_atual = ano_atual - ano_nascimento
    idade_dias = idade_atual * 365
    return idade_dias
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade_em_dias = idade_em_dias(ano_nascimento)
print(f"Sua idade em dias é: {idade_em_dias} dias")