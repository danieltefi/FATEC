n = int(input('Digite um número: '))

divisores = []

for i in range(1, (n//2) + 1):
    if n % i == 0:
        divisores.append(i)

soma = sum(divisores)

if soma == n:
    print(f'{n} é um número perfeito')
else:
    print(f'{n} não é um número perfeito')