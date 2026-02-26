n1 = input('Digite um número: ')
n1 = int(n1)
n2 = input('Digite outro número: ')
n2 = int(n2)
n3 = input('Digite mais um número: ')
n3 = int(n3)

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Esses numeros formam um triângulo')

    if n1 == n2 == n3:
        print('Triângulo equilátero')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')

else:
    print('Esses números não formam um triângulo')