limite = int(input('Digite um número (inteiro) limite que a soma pode atingir: '))
soma = 0
i = 1

while soma <= limite:
    soma = soma + i
    i = i + 1

print(f'A soma dos números naturais até atingir o limite de {limite} é: {soma}')