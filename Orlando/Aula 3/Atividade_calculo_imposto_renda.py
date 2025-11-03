salario = input('Qual seu salário bruto?: ')
salario = float(salario)

if salario <= 1900:
    print('Isento')

elif salario < 2800:
    print('7.5%')
    imposto = salario * 0.075
    print(f'O valor do imposto é: R$ {imposto}')

elif salario < 3700:
    print('15%')
    imposto = salario * 0.150
    print(f'O valor do imposto é: R$ {imposto}')

elif salario < 4600:
    print('22.5%')
    imposto = salario * 0.225
    print(f'O valor do imposto é: R$ {imposto}')

else:
    print('27.5%')
    imposto = salario * 0.275
    print(f'O valor do imposto é: R$ {imposto}')