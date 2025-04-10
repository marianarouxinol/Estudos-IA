def senha_forte(senha):
    return len(senha) >= 8 and any(char.isdigit() for char in senha)

while True:
    senha = input("Digite uma senha forte (mínimo 8 caracteres e pelo menos 1 número) ou 'sair' para encerrar: ")
    
    if senha.lower() == "sair":
        print("Encerrando...")
        break

    if senha_forte(senha):
        print("Senha validada com sucesso!")
        break
    else:
        print("Senha fraca. Tente Tente outra vez!.")