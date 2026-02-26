n = int(input('Digite um número para exibir a sequência Fibonacci desse número: '))
anterior = 0
atual = 1
sequencia = ''

for i in range(n):
    sequencia = sequencia + str(anterior) + ' '
    soma = anterior + atual
    anterior = atual
    atual = soma

print(f'A sequência Fibonacci de {n} é: {sequencia}')