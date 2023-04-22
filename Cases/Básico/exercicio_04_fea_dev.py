##### SEU CODIGO COMECA AQUI #####

while True:

    # Coleta os inputs do usuário
    espessura = float(input("Espessura: "))
    absorcao = float(input("Absorção: "))

    # Verifica a espessura
    if espessura < 0.1:
        print("O papel produzido é muito fino")

    elif espessura > 1.5:
        print("O papel é muito grosso")
    
    elif 0.1 <= espessura <= 1.5:
        print(" espessura OK!")

    # Verfica a absorção
    if absorcao > 6:
        print("O papel é pouco absorvente")

    elif absorcao < 6:
        print("absorção OK!")

    # Verifica a escolha do usuário
    while True:
        print("voce quer continuar a avaliação? (s/n)")
        escolha = input("Escolha: ").lower() # Coleta o input -- escolha -- do usuário

        if escolha == "n":
            break

        elif escolha == "s":
            break

        else:
            print("Entrada inválida!")
    
    if escolha == "n":
        break

    else:
        continue
            