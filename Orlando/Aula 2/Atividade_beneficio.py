idade = input("Digite sua idade: ")
idade = int(idade)
salario = input ("Digite seu salário: ")
salario = int(salario)

if idade > 18 and salario <= 2000 or idade >= 60:
    print("Possui direito")
else:
        print("Não possui direito")