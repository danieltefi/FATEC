n = input('Digite um número (0 para sair): ')
n = int(n)
soma = 0

while n != 0:
    soma = soma + n
    n = input('Digite um número (0 para sair): ')
    n = int(n)

print(f'A soma é: {soma}')    