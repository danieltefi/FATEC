import random

numero_secreto = random.randint(0, 10)
numero_usuario = -1

while numero_usuario != numero_secreto:

    numero_usuario = input('Adivinhe um número entre 0 a 10: ')
    numero_usuario = int(numero_usuario)

    if numero_usuario > numero_secreto:
        print('Número muito alto. Tente novamente!')

    elif numero_usuario < numero_secreto:
        print('Numero muito baixo. Tente novamente!')

else:
    print('Parabéns, você acertou!!')