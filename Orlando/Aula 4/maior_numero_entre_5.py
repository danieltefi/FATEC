numero1 = input('Digite um numero: ')
numero1 = int(numero1)

numero2 = input('Digite outro numero: ')
numero2 = int(numero2)

numero3 = input('Digite outro numero: ')
numero3 = int(numero3)

numero4 = input('Digite outro numero: ')
numero4 = int(numero4)

numero5 = input('Digite outro numero: ')
numero5 = int(numero5)

if numero1 >= numero2 and numero1 >= numero3 and numero1 >= numero4 and numero1 >= numero5:
    print(f'O maior numero é: {numero1}')

elif numero2 >= numero1 and numero2 >= numero3 and numero2 >= numero4 and numero2 >= numero5:
    print(f'O maior numero é: {numero2}')

elif numero3 >= numero1 and numero3 >= numero2 and numero3 >= numero4 and numero3 >= numero5:
    print(f'O maior numero é: {numero3}')

elif numero4 >= numero1 and numero4 >= numero2 and numero4 >= numero3 and numero4 >= numero5:
    print(f'O maior numero é: {numero4}')

elif numero5 >= numero1 and numero5 >= numero2 and numero5 >= numero3 and numero5 >= numero4:
    print(f'O maior numero é: {numero5}')

else:
    print('Os números dgitados sao iguais')