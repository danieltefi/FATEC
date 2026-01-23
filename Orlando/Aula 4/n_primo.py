n = int(input('Digite um número: '))

if n <= 0:
    print('Digite um número inteiro e positivo')
else:
    total_divisores = 0

    for i in range(1, n + 1):
        if n % i == 0:
            total_divisores = total_divisores + 1
    
    if total_divisores == 2:
        print(f'{n} é primo')
    else:
        print(f'{n} não é primo, ele tem {total_divisores} divisores')