saque = input('Digite o valor do saque em R$: ')
saque = int(saque)

notas = [100, 50, 20, 10]
notas_sacadas = {}

for nota in notas:
    if saque >= nota:
        quantidade = saque // nota
        saque = saque % nota

        notas_sacadas[nota] = quantidade
        print('Saque efetuado com sucesso!')
        print(f'{quantidade} nota(s) de R$ {nota}')

        if saque > 0:
            print(f'Sobrou um valor de R$ {saque} que não pode ser sacado devido a notas faltantes')