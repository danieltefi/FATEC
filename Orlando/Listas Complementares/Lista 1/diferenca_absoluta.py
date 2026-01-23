numero1 = input('Digite um número: ')
numero1 = int(numero1)
numero2 = input('Digite outro número: ')
numero2 = int(numero2)

diferenca = numero1 - numero2

if diferenca < 0:
    diferenca_absoluta = diferenca * -1

else:
    diferenca_absoluta = diferenca

print(f'A diferença absoluta entre {numero1} e {numero2} é: {diferenca_absoluta}')