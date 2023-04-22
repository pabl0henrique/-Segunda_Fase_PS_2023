##### SEU CODIGO COMECA AQUI #####
import random

bolas = {
    "Cor": ["Amarela","Azul","Vermelha"],
    "Quantidade": [92,54,24]
}

#### EXERCICIO A ####

# Para rodar, basta apagar as aspas ' '

'''
print(f"A probabilidade é {'%.2f' % (100*((bolas['Quantidade'][2] - 3)/(sum(bolas['Quantidade']) - 3)))}")
'''

#### EXERCICIO B ####

# Para rodar, basta apagar as aspas ' '

'''
rounds = int(input("rounds: ")) # Coleta do Input  do usuário

# Variáveis de controle  
yellow = 0
blue = 0
red = 0
count = 1

if rounds > 1 and rounds <= 170:

    while count <= rounds:
        choice = random.choices(bolas["Cor"],bolas["Quantidade"],k = 1) # Variável armazena as probabilidades reais

        # Condicionais... caso a cor seja X
        if choice == ['Amarela']:
            print(f"Round {count}: {choice}")

            if bolas["Quantidade"][0] == 0:
                continue

            else:
                bolas['Quantidade'][0] -= 1
                yellow += 1

        elif choice == ['Azul']:
            print(f"Round {count}: {choice}")

            if bolas["Quantidade"][1] == 0:
                continue

            else:
                bolas['Quantidade'][1] -= 1
                blue += 1

        elif choice == ['Vermelha']:
            print(f"Round {count}: {choice}")

            if bolas["Quantidade"][2] == 0:
                continue

            else:
                bolas['Quantidade'][2] -= 1
                red += 1

        # Mostra a quantidade de bolas sorteadas
        if count == rounds:
            print(f"\nForam sorteadas:\n{yellow} bolas Amarelas\n{blue} bolas Azuis\n{red} bolas Vermelhas")
            print(bolas["Quantidade"])
            break

        count += 1
else:
    print("Não houve sorteio")
'''    