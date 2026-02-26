numero1 = input("Digite um número: ")
numero1 = int(numero1)
numero2 = input("Digite outro número: ")
numero2 = int(numero2)

if numero1 > numero2:
    print(f"O maior número é: {numero1}")
if numero2 > numero1:
    print(f"O maior número é: {numero2}")
if numero1 == numero2:
    print("Os dois números são iguais")