temperatura = input('Digite uma temperatura em ºC: ')
temperatura = int(temperatura)

if temperatura <= 15:
    print('Frio!')

elif temperatura < 25:
    print('Agradável')

else:
    print('Quente!')