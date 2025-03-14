def calcular_gorjeta():
    print("Bem-vindo ao calculador de gorjetas!")
    
    # Obter o valor total da conta
    while True:
        try:
            valor_conta = float(input("Digite o valor total da conta (R$): "))
            if valor_conta <= 0:
                raise ValueError("O valor da conta deve ser maior que zero.")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

    # Obter a porcentagem da gorjeta
    while True:
        try:
            porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))
            if porcentagem_gorjeta < 0:
                raise ValueError("A porcentagem da gorjeta não pode ser negativa.")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

    # Calcular o valor da gorjeta
    gorjeta = (valor_conta * porcentagem_gorjeta) / 100
    valor_total = valor_conta + gorjeta

    print(f"\nO valor da gorjeta é: R$ {gorjeta:.2f}")
    print(f"O valor total da conta com a gorjeta é: R$ {valor_total:.2f}")
    
    # Perguntar se a gorjeta será dividida entre várias pessoas
    while True:
        try:
            num_pessoas = int(input("Você gostaria de dividir a gorjeta entre várias pessoas? (Digite o número de pessoas ou 1 para não dividir): "))
            if num_pessoas < 1:
                raise ValueError("O número de pessoas deve ser pelo menos 1.")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")
    
    # Dividir a gorjeta entre as pessoas, se for o caso
    if num_pessoas > 1:
        gorjeta_por_pessoa = gorjeta / num_pessoas
        total_por_pessoa = valor_total / num_pessoas
        print(f"\nCada pessoa vai pagar R$ {total_por_pessoa:.2f}, incluindo R$ {gorjeta_por_pessoa:.2f} de gorjeta.")
    else:
        print("\nA gorjeta não será dividida entre várias pessoas.")

# Chama a função para calcular a gorjeta
calcular_gorjeta()