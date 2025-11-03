salario = input('Digite seu salário: ')
salario = float(salario)

if salario < 2000.00:
    print('Recebe bônus de 20%')

elif salario < 5000.00:
    print('Recebe bônus de 10%')

else:
    print('Recebe bônus de 5%')