sala = [[0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0]
        ]

partida = [0,0]
chegada = [4,4]

fila = []
no_atual = partida
while True:
    for possibilidades in [[[no_atual[0], no_atual[1]+1]]
                           [no_atual[0]+1, no_atual[1]]
                           [no_atual[0], no_atual[1]-1]
                           [no_atual[0]-1, no_atual[1]]
                           ]