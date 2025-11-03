numeros = []

for i in range(10):
    numeros.append(int(input(f'Digite o {i + 1}º número: ')))

positivos = 0

for i in numeros:
    if i >= 0:
        positivos = positivos + 1

print(f'A quantidade de números positivos é: {positivos}')