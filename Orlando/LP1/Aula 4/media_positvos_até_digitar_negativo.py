numeros = []
positivos = []
soma = 0
contador_positivos = 0

while True:
    try:
        numero = input('Digite um número: ')
        numero = int(numero)
        if numero < 0:
            break
        numeros.append(numero)
        
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números inteiros.")

for x in numeros:
    if x >= 0:
        positivos.append(x)

for y in positivos:
    soma = soma + y

for u in positivos:
    contador_positivos = contador_positivos + 1

if contador_positivos > 0:
    media = soma / contador_positivos
else:
    media = 0

print(f'A média dos números postivos é: {media}')