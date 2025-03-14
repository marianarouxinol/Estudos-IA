ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f"{ano} é uma no bissexto.")
        else:
            print(f"{ano} não é um ano bissexto.")
    else:
        print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é uma ano bissexto.")    