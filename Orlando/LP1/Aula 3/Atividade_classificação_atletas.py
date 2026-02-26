idade = input('Digite sua idade: ')
idade = int(idade)

if idade <= 12:
    print('Categoria infantil')

elif idade <= 17:
    print('Categoria juvenil')

elif idade <= 40:
    print('Categoria Adulto')

else:
    print('Categoria veterano')