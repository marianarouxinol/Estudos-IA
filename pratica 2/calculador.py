while True:

    try:

        num1 = float(input("Digite o primeiro número: "))

        num2 = float(input("Digite o segundo número: "))


        operacao = input("Escolha a operação (+, -, *, /): ")


        if operacao == "+":

            resultado = num1 + num2

        elif operacao == "-":

            resultado = num1 - num2

        elif operacao == "*":

            resultado = num1 * num2

        elif operacao == "/":

            if num2 == 0:

                raise ZeroDivisionError("Não é possível dividir por zero.")

            resultado = num1 / num2

        else:

            raise ValueError("Operação inválida. Escolha entre +, -, * ou /.")


        print(f"Resultado: {resultado:.2f}")

        break


    except ValueError as e:

        print(f"Erro: {e}. Tente novamente.")

    except ZeroDivisionError as e:

        print(f"Erro: {e}. Tente novamente.")