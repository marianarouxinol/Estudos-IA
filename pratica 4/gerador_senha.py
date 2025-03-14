import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha

"""string.ascii_letters → Letras maiúsculas e minúsculas (A-Z, a-z).
string.digits → Números de 0 a 9.
string.punctuation → Caracteres especiais (!@#$%^&*(), etc.).
random.choice(caracteres) → Escolhe aleatoriamente um caractere da lista.
join() → Junta todos os caracteres gerados em uma única string."""

tamanho_senha = int(input("Digite o tamanho da senha: "))
nova_senha = gerar_senha(tamanho_senha)
print(f"A senha gerada é: {nova_senha}")
