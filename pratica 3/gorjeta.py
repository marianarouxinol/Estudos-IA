def calcular_gorjeta (valor_conta, porcetagem_gorjeta):
    gorjeta = valor_conta * (porcetagem_gorjeta / 100)
    return round(gorjeta, 2)
total_conta = 100.00
porcetagem = 15
gorjeta = calcular_gorjeta(total_conta, porcetagem)
print(f"Para a conta que ficou em R$ {total_conta:.2f}, a gorjeta de {porcetagem}% é de R$ {gorjeta:.2f}")