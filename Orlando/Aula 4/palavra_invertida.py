palavra = input('Digite uma palavra: ')
invertida = ""
comprimento = 0

for x in palavra:
    comprimento = comprimento + 1

indice = comprimento - 1

while indice >= 0:
    caractere = palavra[indice]
    invertida = invertida + caractere
    indice = indice - 1

print(f'A {palavra} invertida é: {invertida}')