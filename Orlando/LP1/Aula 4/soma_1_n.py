soma = 0

n = input('Digite um número: ')
n = int(n)

for i in range(1, n +1):
    soma = soma + i
    
print(f'A soma de 1 até {n} é: {soma}')