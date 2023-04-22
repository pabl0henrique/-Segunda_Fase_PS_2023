##### SEU CODIGO COMECA AQUI #####

# Coleta os inputs do usuário
nota_media = float(input("Nota média: "))
frequencia = float(input("Frequência: "))

# Verifica os inputs do usuário
if nota_media > 5 and frequencia >= 70:
    print("Aluno aprovado")

elif 3 < nota_media < 4.9 and frequencia >= 70:
    print("Aluno em recuperação")

elif nota_media < 3 and frequencia >= 70:
    print("O aluno está reprovado por média")

elif nota_media > 3 and frequencia < 70:
    print("Aluno reprovado por falta")

elif nota_media < 3 and frequencia < 70:
    print("Aluno reprovado por falta e por média")