import random

numero_sorteado = random.randint(1, 50)

usuario = int(input('Tente adivinhar o número gerado pelo computador entre 1 e 50 (inteiro): '))

while usuario != numero_sorteado:
    if usuario < numero_sorteado:
        print(f'Voçê errou! o número é maior que {usuario}')
    else:
        print(f'Voçê errou! o número é menor que {usuario}')
    
    usuario = int(input('Tente outro número: '))

if usuario == numero_sorteado:
    print(f'Parabéns, voçê acertou! O número era {numero_sorteado}')
