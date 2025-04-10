import pandas
import csv

arquivo_csv = "dados_pessoas.csv"

dados = [
    ["Nome","Idade","Cidade"],
    ["Ricardo","47","Assis"]
]

with open(arquivo_csv, "w", encoding="utf-8") as arquivo:
    gravar = csv.writer(arquivo)
    gravar.writerows(dados)
    print(f"Dados gravados em {arquivo_csv}")
