dia = input('Digite um dia do mês: ')
dia = int(dia)

mes = input('Digite o mês em número: ')
mes = int(mes)

ano = input('Digite um ano: ')
ano = int(ano)

mes_formatado = ''

if mes == 1:
    mes_formatado = 'Janeiro'

elif mes == 2:
    mes_formatado = 'Fevereiro'

elif mes == 3:
    mes_formatado = 'Março'

elif mes == 4:
    mes_formatado = 'Abril'

elif mes == 5:
    mes_formatado = 'Maio'

elif mes == 6:
    mes_formatado = 'Junho'

elif mes == 7:
    mes_formatado = 'Julho'

elif mes == 8:
    mes_formatado = 'Agosto'

elif mes == 9:
    mes_formatado = 'Setembro'

elif mes == 10:
    mes_formatado = 'Outubro'

elif mes == 11:
    mes_formatado = 'Novembro'

elif mes == 12:
    mes_formatado = 'Dezembro'

print(f'{dia} de {mes_formatado} de {ano}')