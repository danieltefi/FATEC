divisores = []

numero = input('Digite um número positivo: ')
numero = int(numero)

for n in range(1, numero + 1):
    if numero % n == 0:
        divisores.append(n)

print(f'Os divisores de {numero} são: {divisores}')