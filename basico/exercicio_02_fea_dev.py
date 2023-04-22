##### SEU CODIGO COMECA AQUI #####

empresa = 'Dunder Mifflin paper company'

##### Exercício A #####

# Para rodar, basta apagar as aspas ' '

'''
empresa_invertido = []

count = 0
for i in empresa:
    empresa_invertido.append(empresa[(len(empresa) - 1) - count])
    count += 1

print(''.join(empresa_invertido))
'''

##### Exercício B #####

# Para rodar, basta apagar as aspas ' '

'''
print(empresa[0:14])
'''

##### Exercício C #####

# Para rodar, basta apagar as aspas ' '

'''
caracteres = len(empresa)
count = 0
for i in empresa:
    if empresa[count] == ' ':
        letras = caracteres - 1
    count += 1

print (f"O nome '{empresa}' possui {letras} letras.")
'''

##### Exercício D #####

# Para rodar, basta apagar as aspas ' '
'''
count = 1
for i in empresa:
    print(empresa[0:count])
    count +=1
'''