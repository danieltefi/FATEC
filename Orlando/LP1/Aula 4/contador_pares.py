numeros = []

for i in range(10):
    numeros.append(int(input(f'Digite o {i +1}º número: ')))

contador_pares = 0

for i in numeros:
    if i % 2 == 0:
        contador_pares = contador_pares + 1

print(f'A quantidade de números pares é: {contador_pares}')