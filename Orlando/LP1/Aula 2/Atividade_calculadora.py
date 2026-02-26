peso = input("Digite seu peso em kg: ")
peso = float(peso)
altura = input("Digite sua altura em m: ")
altura = float(altura)

imc = peso / altura ** 2

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("Peso normal")
elif imc < 29.9:
    print("Sobrepeso")
elif imc < 34.9:
    print ("Obesidade grau 1")
elif imc < 39.9:
    print("Obsidade grau 2")
else:
    print("Obsidade grau 3")