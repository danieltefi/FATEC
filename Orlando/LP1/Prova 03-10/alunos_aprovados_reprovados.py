quantidade_alunos = int(input("Digite a quantidade de alunos: "))

aprovados = 0
reprovados = 0

for i in range(quantidade_alunos):
    print(f"\n--- Aluno {i + 1} ---")

    nota1 = float(input(f"Digite a primeira nota do aluno {i + 1}: "))
    nota2 = float(input(f"Digite a segunda nota do aluno {i + 1}: "))

    media = (nota1 + nota2) / 2
    print(f"A média do aluno {i + 1} é: {media:.2f}")

    if media >= 7.0:
        aprovados = aprovados + 1 
        print("Situação: Aprovado")
    else:
        reprovados = reprovados + 1 
        print("Situação: Reprovado")

print(f"Total de alunos aprovados: {aprovados}")
print(f"Total de alunos reprovados: {reprovados}")