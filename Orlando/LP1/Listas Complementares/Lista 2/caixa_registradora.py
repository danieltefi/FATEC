precos = []
soma = 0
i = 1

while True:
    preco = float(input(f'Digite o valor do {i}º produto ou 0 para sair: '))
    if preco == 0:
        break

    precos.append(preco)
    i = i + 1

for preco in precos:
    soma = soma + preco

print(f'O valor da soma dos produtos é: {soma}')

if soma > 100:
    soma = soma * 0.90
    print('Desconto de 10% aplicado!')
else:
    print('Valor da compra não atingiu limite para desconto!')

print(f'Total da compra para pagamento: R$ {soma}')