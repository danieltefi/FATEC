numeros = []

for i in range(5):
    numeros.append(int(input(f'Digite o {i + 1}º número: ')))

menor_numero = numeros[0]

for num  in numeros:
    if num < menor_numero:
        menor_numero = num

print(f'O menor número é: {menor_numero}')