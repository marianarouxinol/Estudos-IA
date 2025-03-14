temp = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ")
destino = input("Digite a unidade de destino (C, F ou K): ")

if origem == destino:
    resultado = temp
elif origem == "C":
    if destino == "F":
        resultado =(temp * 9/5) + 32
elif origem == "F":
    if destino == "C":
        resultado =(temp * 9/5) + 32