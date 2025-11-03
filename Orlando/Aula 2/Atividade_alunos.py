nota = input("Digite sua nota de 0 a 100: ")
nota = int(nota)

if nota >= 90:
    print("Aproado com Excelência")
elif nota >=70:
        print("Aprovado")
elif nota >=50:
        print("Recuperação")
else:
    print("Reprovado")
