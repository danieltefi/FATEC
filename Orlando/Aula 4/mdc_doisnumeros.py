n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

a = n1
b = n2

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(f'O MDC entre {n1} e {n2} é: {a}')