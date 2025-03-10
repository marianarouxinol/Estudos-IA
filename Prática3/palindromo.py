def palindromo(texto):
    texto_limpo="".join(char.lower() for char in texto if char.isalnum())
    return texto_limpo == texto_limpo[::-1]
frase = "A cara rajada da jararaca"
resultado = palindromo(frase)
resultado = "Sim" if resultado else "Não"
print(f'{frase}é um palíndromo: {resultado}')
