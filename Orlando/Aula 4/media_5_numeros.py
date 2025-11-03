numeros = []

for i in range(5):
    numeros.append(int(input(f'Digite o {i +1}º número: ')))

soma = 0
contador = 0

for numero in numeros:
    soma = soma +  numero
    contador = contador + 1

media = soma / contador

print(f'A média dos números é: {media}')