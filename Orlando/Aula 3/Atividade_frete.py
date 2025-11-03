valor = input('Qual o valor da compra?: ')
valor = int(valor)

if valor > 100:
    print('Frete grátis')

else:
    print('R$ 15.00 reais de frete')