nomes = ['José', 'Maria', 'Pedro', 'Paula', 'João']

nome = input('Informe um nome: ')
nome_formatado = nome.capitalize()

if nome_formatado in nomes:
    print(f'{nome} está na lista')

else:
    print(f'{nome} não está na lista')