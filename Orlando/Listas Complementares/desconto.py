preco = input('Digite o preço do produto em R$: ')
preco = float(preco)

desconto = preco * 0.1

valor_final = preco - desconto

print(f'Com 10% de desconto, você deverá pagar R$: {valor_final}')