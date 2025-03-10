def calcular_gorjeta(valor_conta, percentual=10):
    gorjeta = (valor_conta * percentual) / 100
    total_com_gorjeta = valor_conta + gorjeta
    return gorjeta, total_com_gorjeta

valor_conta = float(input("Digite o valor da conta: R$ "))
percentual = float(input("Digite a porcentagem da gorjeta (padrão 10%): ") or 10)

gorjeta, total = calcular_gorjeta(valor_conta, percentual)

print(f"Gorjeta:R$ {gorjeta:.2f}")
print(f"Total a pagar: R$ {total:.2f}")