##### SEU CODIGO COMECA AQUI #####

the_office = {
    "Nome": ["Michael","Pam","Dwight","Stanley","Ryan"],
    "Salário": [9000,3000,4500,6000,500],
    "Anos de trabalho": [18,11,7,30,1]
}

count = 0
for i in the_office["Anos de trabalho"]:

    # Verfica os anos de trabalho
    if the_office["Anos de trabalho"][count] >= 5 and the_office["Anos de trabalho"][count] <= 10:
        print(f"O funcionário {the_office['Nome'][count]} passará a ganhar U$ {the_office['Salário'][count] * 1.025}")

    elif the_office["Anos de trabalho"][count] >= 11 and the_office["Anos de trabalho"][count] <= 15:
        print(f"O funcionário {the_office['Nome'][count]} passará a ganhar U$ {the_office['Salário'][count] * 1.05}")

    elif the_office["Anos de trabalho"][count] >= 16 and the_office["Anos de trabalho"][count] <= 25:
        print(f"O funcionário {the_office['Nome'][count]} passará a ganhar U$ {the_office['Salário'][count] * 1.07}")

    elif the_office["Anos de trabalho"][count] > 25:
        print(f"O funcionário {the_office['Nome'][count]} passará a ganhar U$ {the_office['Salário'][count] * 1.10}")

    else:
         print(f"O funcionário {the_office['Nome'][count]} não receberá aumento.")

    count += 1   