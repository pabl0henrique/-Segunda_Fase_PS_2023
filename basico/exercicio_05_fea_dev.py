##### SEU CODIGO COMECA AQUI #####

folhetos = {
    "Instituto":["FEA","Física","IME","POLI"],
    "Qnt. Pacotes":[8,4,6,21]
}

count = 0
for i in folhetos["Qnt. Pacotes"]:

    # Verifica se a quantidade de pacotes é maior ou igual a 2
    if folhetos["Qnt. Pacotes"][count] >= 2:
        desconto = (folhetos["Qnt. Pacotes"][count] * 0.03)/2 # Variável que armazena o valor do desconto

        # Verifica se o valor do desconto é maior que 30%, se for, o desconto fica limitado a 30%
        if desconto > 0.3:

            # Variável que armazena o valor final do valor dos pacotes, cujo o desconto igual a 30%
            valor_final = folhetos["Qnt. Pacotes"][count] * 60 - folhetos["Qnt. Pacotes"][count] * 60 * 0.7
            print(f"Para o instituto {folhetos['Instituto'][count]} o valor dos pacotes, aplicando o desconto de 30%, sairá US$ {'%.2f'%valor_final}")
        else:

            # Variável que armazena o valor final do valor dos pacotes, cujo o desconto seja menor que 30%
            valor_final = folhetos["Qnt. Pacotes"][count] * 60 - folhetos["Qnt. Pacotes"][count] * 60 * desconto
            print(f"Para o instituto {folhetos['Instituto'][count]} o valor dos pacotes, aplicando o desconto de {'%.f'%(desconto * 100)}%, sairá US$ {'%.2f'%valor_final}")
    
    count += 1