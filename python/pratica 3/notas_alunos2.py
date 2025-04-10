notas = []

while True:
    entrada = input("Digite a nota (0 a 10) ou 'fim' para encerrar: ")

    if entrada.lower() == 'fim':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")

if notas:
    media = sum(notas) / len(notas)
    print(f"A média da turma é: {media:.2f}")
else:
    print("Nenhuma nota foi registrada.")