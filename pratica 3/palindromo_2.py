def eh_palindromo(texto):
    # Remover espaços e pontuação
    texto = ''.join(caractere for caractere in texto.lower() if caractere.isalnum())
    
    # Verificar se a string é igual de trás para frente
    return texto == texto[::-1]

while True:
    palavra_ou_frase = input("Digite uma palavra ou frase (ou 'fim' para sair): ")
    if palavra_ou_frase.lower() == "fim":
        break
    
    if eh_palindromo(palavra_ou_frase):
        print("Sim")
    else:
        print("Não")