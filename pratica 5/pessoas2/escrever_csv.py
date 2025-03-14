import csv

arquivo_csv = "pessoas.csv"

dados = [
    ["Nome", "Idade", "Cidade"], 
    ["Talyta", 29, "Manaus"],
    ["Lavini", 27, "São Paulo"],
    ["Debora", 26, "Fortaleza"]
]
with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)

print(f"Arquivo '{arquivo_csv}' criado com sucesso!")