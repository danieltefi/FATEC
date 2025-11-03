numero = input('Digite um número: ')
numero = int(numero)

if numero < 0:
    print(f'O número {numero} é negativo')

elif numero > 0:
    print(f'O número {numero} é positivo')

else:
    print(f'O número {numero} é zero')