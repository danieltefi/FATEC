quantidade = int(input('Quantas notas voçê deseja calcular a média?: '))
notas = []
soma = 0

for i in range(1, quantidade + 1):
    nota = float(input(f'Digite a {i}ª nota: '))
    notas.append(nota)

for nota in notas:
    soma = soma + nota

media = soma / quantidade

print(f'A média das notas é: {media}')

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')