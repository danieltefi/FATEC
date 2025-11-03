nota1 = input('Digite uma nota: ')
nota1 = int(nota1)
nota2 = input('Digite outra nota: ')
nota2 = int(nota2)
nota3 = input('Digite mais uma nota: ')
nota3 = int(nota3)

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print('Aprovado')

else:
    print('Reprovado')