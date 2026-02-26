nota = input("Digite sua nota de 0 a 10: ")
nota = int(nota)

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")