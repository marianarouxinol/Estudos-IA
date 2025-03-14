def analise_numero():
    pares = 0
    impares = 0
    while True:
        entrada = input("Digite um núemro inteiro ou fim para sair: ")
        if entrada.lower() == "fim":
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} é par.")
                pares += 1
            else:
                print(f"{numero} é impar.")
                impares += 1
        except ValueError:
            print("Erro! Digite um número inteiro.")
            continue
    print(f"Resultado final: ")
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
analise_numero()
