valor = input('Digite um valor inteiro: ')
valor = int(valor)

if valor < 0:
    print('Valor inválido. Digite um número positivo')
elif valor == 0:
    print('Não é necessário notas para o valor informado')
else:
    print('\nNotas necessárias: ')

    notas = [100, 50, 20, 10, 5, 2, 1]
    for nota in notas:
        quantidade = valor // nota
        if quantidade > 0:
            print(f'{quantidade} nota(s) de R$ {nota}')

            valor = valor % nota