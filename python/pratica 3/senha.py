def verifica_senha():
    while True:
        senha = input("Digite uma senha (ou SAIR para encerrar): ")
        if senha == "SAIR":
            print("Programa encerrado")
            break
        if len(senha) < 8:
            print("Senha fraca: deve ter no minino 8 caracteres.")
            continue
        if not any(caractere.isdigit() for caractere in senha):
            print("Senha fraca: deve conter pelo menos um número.")
            continue
        print("Senha forte e válida!")
        break
verifica_senha()