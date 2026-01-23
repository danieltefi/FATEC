numeros = []
par = []
impar = []
soma = 0

for i in range(1, 11):
    num = int(input(f'Digite o {i}º número: '))

    numeros.append(num)

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

quantidade_pares = len(par)
quantidade_impares = len(impar)

for n in par:
    soma = soma + n

print(f'Temos {quantidade_pares} números pares, {quantidade_impares} números ímpares. \nA soma dos pares é: {soma}')