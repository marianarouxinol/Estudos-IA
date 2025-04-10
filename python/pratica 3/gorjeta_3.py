def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    return valor_conta * (porcentagem_gorjeta / 100)

valor_conta = 200.00
porcentagem_gorjeta = 15

gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
print(f"Gorjeta: R$ {gorjeta:.2f}")