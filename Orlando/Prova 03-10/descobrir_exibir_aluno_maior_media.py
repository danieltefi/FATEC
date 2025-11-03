alunos = (
    {'nome': 'Ana', 'notas': [8, 7, 9]},
    {'nome': 'Bruno', 'notas': [5, 6, 7]},
    {'nome': 'Carla', 'notas': [9, 9, 10]},
    {'nome': 'Diego', 'notas': [6, 5, 6]},
    {'nome': 'Elisa', 'notas': [7, 8, 7]},
    {'nome': 'Felipe', 'notas': [10, 9, 10]},
    {'nome': 'Gustavo', 'notas': [5, 6, 5]},
    {'nome': 'Helena', 'notas': [8, 9, 8]},
    {'nome': 'Igor', 'notas': [7, 7, 6]},
    {'nome': 'Julia', 'notas': [9, 8, 9]},
)

melhor_aluno = None
notas_melhor_aluno = []
maior_media = - 1

for aluno in alunos:
    soma_notas = 0
    quantidade_notas = 0

    for nota in aluno['notas']:
        soma_notas += nota
        quantidade_notas += 1
        
    if quantidade_notas > 0:
        media_atual = soma_notas / quantidade_notas
    else:
        media_atual = 0
        
    if media_atual > maior_media:
        maior_media = media_atual
        melhor_aluno = aluno['nome']
        notas_melhor_aluno = aluno['notas']

print('Aluno com maior média: ' + melhor_aluno)
print('Notas: ' + str(notas_melhor_aluno))
print('Média: '+ str(maior_media))