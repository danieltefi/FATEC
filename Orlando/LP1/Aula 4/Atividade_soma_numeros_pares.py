numero = input('Digite um número: ')
numero = int(numero)
soma = 0

for i in range(2, numero + 1, 2):
    print(str(i))
    soma = soma + i

print(f'A soma dos números pares de 1 até {numero} é: {soma}')