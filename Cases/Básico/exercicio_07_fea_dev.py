##### SEU CODIGO COMECA AQUI #####
import pandas
import calendar

##### EXERCICIO A #####

# Para rodar, basta apagar as aspas ' '

'''
cadastro = {
    "Nome":[],
    "Idade":[]
}

# Inicio programa
while True:
    nome = input("\nNome: ")
    idade = int(input("Idade: "))

    # Adiciona os inputs nos vetores "Nome" e "Idade"
    cadastro["Nome"].append(nome)
    cadastro["Idade"].append(idade)

    # Bloco de interrupcao do programa
    while True:
        print("\nVocê quer continuar a adicionar dados? (s/n)")
        escolha = input("Escolha: ").lower()

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

# Criacao do Data Frame para visualizacao dos dados
cadastro_df = pandas.DataFrame(cadastro)

print(f"\nDados cadastrados:\n\n{cadastro_df}")

# Numero de pessoas cadastradas
print(f"\n{len(cadastro['Nome'])} pessoa(s) fora(m) cadastrada(s).")
  
# Mostra a pessoa mais velha e a mais nova e define a media
media = 0 
count = 0
for i in cadastro["Idade"]:
    if cadastro["Idade"][count] == max(cadastro["Idade"]):
        print(f"\n{cadastro['Nome'][count]} é a pessoa mais velha com {cadastro['Idade'][count]} anos de idade.")

    if cadastro["Idade"][count] == min(cadastro["Idade"]):
        print(f"\n{cadastro['Nome'][count]} é a pessoa mais nova com {cadastro['Idade'][count]} anos de idade.") 
    
    media += cadastro["Idade"][count]
    count += 1

# mostra a media
print(f"\nA idade média é {media/count}")
'''

##### EXERCICIO B #####

# Para rodar, basta apagar as aspas ' '

'''
data = input("Data: ")

dd = int(data[0:2])
mm = int(data[3:5])
yyyy = int(data[6:10])
'''

##### EXERCICIO C #####

# Para rodar, basta apagar as aspas ' '

'''
print(f"\n{calendar.month(yyyy,mm,dd)}")
'''
