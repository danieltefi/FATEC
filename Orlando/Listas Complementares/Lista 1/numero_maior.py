numero1 = input('Digite um número: ')
numero1 = int(numero1)

numero2 = input('Digite outro número: ')
numero2 = int(numero2)

if numero1 > numero2:
    print(f'O número maior é: {numero1}')

elif numero2 > numero1:
    print(f'O número maior é: {numero2}')

else:
    print('Ambos os numeros são iguais')