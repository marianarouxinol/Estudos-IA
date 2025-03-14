peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite seu altura (m): "))

imc = peso / (altura **2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 24.9:
     print("Classificação: Peso normal")
elif 25 <= imc < 29.9:
     print("Classificação: Peso Sobrepeso")
else:
     print("Classificação: Obesidade")