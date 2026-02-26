idade = input('Digite sua idade: ')
idade = int(idade)

gestante = input('É gestante? (S/N): ')
deficiente = input('É deficiente? (S/N): ')

if deficiente == 'S' or idade >= 60:
    print('Prioridade máxima')

elif gestante == 'S':
    print('Prioridade média')

else:
    print('Atendimento normal')