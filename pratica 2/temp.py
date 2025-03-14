def converter_temperatura(valor, origem, destino):
    if origem == "C" and destino == "F":
        return (valor * 9/5) + 32
    elif origem == "C" and destino == "K":
        return valor + 273.15
    elif origem == "F" and destino == "C":
        return (valor - 32) * 5/9
    elif origem == "F" and destino == "K":
        return (valor - 32) * 5/9 + 273.15
    elif origem == "K" and destino == "C":
        return valor - 273.15
    elif origem == "K" and destino == "F":
        return (valor - 273.15) * 9/5 + 32
    else:
         return valor
valor = float(input("Digite a temperatura: "))
origem = input("Informe a unidade de origem (C, F, K): ").upper()
destino = input("Informe a unidade para conversão (C, F, K): ").upper()

if origem not in ("C", "F", "K") or destino not in ("C", "F", "K"):
    print("Unidade inválida! Use C para Celsius, F para Fahrenheit ou K para Kelvin.")
else:
    resultado = converter_temperatura(valor, origem, destino)
    print(f"Temperatura convertida: {resultado:.2f} {destino}")