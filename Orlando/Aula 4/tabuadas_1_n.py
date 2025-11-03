tabuada = []

n = input('Digite um número: ')
n = int(n)

for x in range(1, n + 1):
    tabuada.append(x)

print(str(x) + 'x' + str(n) + '=' + str(x * n))