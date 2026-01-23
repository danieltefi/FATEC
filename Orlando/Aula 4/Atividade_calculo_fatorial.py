n = input('Digite um número para calcular seu fatorial: ')
n = int(n)

if n <0:
    print('Precisa ser um inteiro positivo')
else:
    fatorial_for = 1

    for i in range(1, n + 1):
        fatorial_for = fatorial_for * i
    print(f'Usando for: {n}! = {fatorial_for}')

    fatorial_while = 1
    contador = 1

    while contador <= n:
        fatorial_while = fatorial_while * contador
        contador = contador + 1
    print(f'Usando while: {n}! = {fatorial_while}')