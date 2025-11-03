numeros = []

for x in range(8):
    numeros.append(int(input(f'Digite o {x + 1}º número: ')))

maior = numeros[0]
menor = numeros[0]

for numero in numeros[1:]:
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print(f'O maior elemente é {maior} e o menor {menor}')