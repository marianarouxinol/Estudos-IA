def calcular():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao not in ('+', '-', '*', '/'):
                raise ValueError("Operação inválida. Escolha entre +, -, * ou /.")

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Erro: divisão por zero não é permitida.")
                resultado = num1 / num2

            print(f"Resultado: {resultado}")
            break  # Encerra o loop após um cálculo bem-sucedido

        except ValueError as ve:
            print(f"Erro de entrada: {ve}. Tente novamente.")
        except ZeroDivisionError as zde:
            print(f"Erro matemático: {zde}. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")

calcular()