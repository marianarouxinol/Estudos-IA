def calculadora():  # Define uma função chamada "calculadora"
    while True:  # Inicia um loop infinito, garantindo que a calculadora continue funcionando até que uma operação válida seja concluída
        try:  
            num1 = float(input("Digite o primeiro número: "))  # Solicita ao usuário o primeiro número e converte para float
            num2 = float(input("Digite o segundo número: "))   # Solicita ao usuário o segundo número e converte para float
            operacao = input("Digite a operação (+, -, *, /): ")  # Solicita ao usuário a operação desejada
            
            # Estrutura condicional para verificar qual operação será realizada
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                resultado = num1 / num2  # Aqui pode ocorrer erro de divisão por zero
            else:
                raise ValueError("Operação inválida")  # Lança um erro se a operação for inválida
            
            print(f"Resultado: {resultado}")  # Exibe o resultado da operação
            break  # Encerra o loop caso a operação seja bem-sucedida

        except ValueError as e:  # Captura erros de valor inválido (ex.: operação errada ou entrada não numérica)
            print(f"Erro: {e}. Tente novamente.")
        except ZeroDivisionError:  # Captura erro de divisão por zero
            print("Erro: Divisão por zero não é permitida. Tente novamente.")

# Chamada da função
calculadora()


"""Explicação dos comandos:
def (Definição de Função) O def é utilizado para definir uma função. Uma função é um bloco de código reutilizável que pode ser chamado sempre que necessário.
Ele permite organizar o código em blocos reutilizáveis e evitar repetições.

while (Laço de Repetição) O while cria um loop que continua rodando enquanto a condição for verdadeira.
Ele é útil quando queremos repetir um bloco de código até que uma determinada condição seja atendida.

try e except (Tratamento de Exceções) O try é usado para tentar executar um bloco de código. Se ocorrer um erro, o except trata esse erro.
Ele impede que o programa pare de funcionar devido a um erro inesperado.

if, elif, else (Estruturas Condicionais) O if verifica se uma condição é verdadeira. O elif permite adicionar verificações extras, e o else define o que fazer se nenhuma das condições for verdadeira.
Ele permite que o código tome decisões com base em diferentes entradas.

raise (Lançamento de Exceções) O raise é usado para lançar um erro manualmente.
Ele é útil para validar dados e impedir que valores inválidos passem despercebidos.

break (Interrupção de Laço) O break interrompe um loop while ou for imediatamente.
Ele permite sair de um loop quando uma condição específica for atingida.

def: Define uma função.
while: Cria um laço de repetição.
try: Tenta executar um bloco de código.
except: Captura e trata erros.
if, elif, else: Permitem tomar decisões baseadas em condições.
raise: Lança erros personalizados.
break: Interrompe um loop.

"""