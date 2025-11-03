nota = input('Informe uma nota de 0 a 10: ')
nota = int(nota)

if nota < 0 or nota > 10:
    print('Nota inválida. Por favor, digite um valor entre 0 e 10.')

elif nota >= 9:
    print('Conceito A')

elif nota >= 7:
    print('Conceito B')

elif nota >= 5:
    print('Conceito C')

elif nota >= 3:
    print('Conceito D')

else:
    print('Conceito E')