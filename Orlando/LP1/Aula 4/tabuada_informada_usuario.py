tabuada = input('Digite o número de uma tabuada: ')
tabuada = int(tabuada)

for x in range(1,11):
    print(str(tabuada) + 'x' + str(x) + '=' + str(tabuada * x))