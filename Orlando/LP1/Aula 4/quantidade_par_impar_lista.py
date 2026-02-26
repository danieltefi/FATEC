numeros = []

for x in range(10):
    numeros.append(int(input(f'Digite o {x + 1}º número: ')))

pares = 0
impares = 0

for n in numeros:
    if n % 2 == 0:
        pares = pares + 1

    else:
        impares = impares + 1
print(f'A lista possui {pares} números pares e {impares} números ímpares')