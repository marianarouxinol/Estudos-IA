from datetime import date

def idade_em_dias(ano):
    ano_atual = date.today().year
    idade_anos = ano_atual - ano
    return idade_anos * 365

ano = int(input("Digite o ano de seu nascimento: "))
print(f"Você tem aproximadamente {idade_em_dias(ano_nascimento)} dias de vida.")
from datetime import date

def idade_em_dias(ano):
    ano_atual = date.today().year
    idade_anos = ano_atual - ano
    return idade_anos * 365

ano = int(input("Digite o ano de seu nascimento: "))
print(f"Você tem aproximadamente {idade_em_dias(ano)} dias de vida.")