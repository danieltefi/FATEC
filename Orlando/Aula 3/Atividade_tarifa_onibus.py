idade = input('Qual sua idade?: ')
idade = int(idade)

estudante = input('É estudante? (S/N): ')

if idade <= 6 or idade >= 65:
    print('Tarifa grátis')

elif estudante.upper() == 'S':
    print('Tarifa com 50% de desconto')

else:
    print('Tarifa normal')
