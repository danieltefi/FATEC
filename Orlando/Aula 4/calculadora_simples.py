n1 = int(input('Digite um número inteiro:'))
n2 = int(input('Digite outro número inteiro:'))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2

escolha_usuario = int(input('Escolha a operação que deseja \n1 Adição \n2 Subtração \n3 Multiplicação \n4 Divisão \n5 Sair: '))

if escolha_usuario == 1:
    print(f'A soma de {n1} + {n2} = {soma}')
elif escolha_usuario == 2:
    print(f'A subtração de {n1} - {n2} = {sub}')
elif escolha_usuario == 3:
    print(f'A multiplicação de {n1} x {n2} = {mult}')
elif escolha_usuario == 4:
    print(f'A divisão de {n1} / {n2} = {div}')
elif escolha_usuario == 5:
    print('Calculadora encerrada')
else:
    print('Opcão Inválida')