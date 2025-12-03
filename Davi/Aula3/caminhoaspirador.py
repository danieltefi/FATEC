from collections import deque

ambiente = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]

def lerSensor(pos):
    x, y = pos
    for i in range(3):
        for j in range(3):
            if ambiente[i][j] == 1:
                print("Sujeira encontrada na posição:", (i, j))
                return (i, j) 
    return pos 

def pensar(pos_inicial, pos_sujeira):

    inicio = [pos_inicial[0], pos_inicial[1]]
    objetivo = [pos_sujeira[0], pos_sujeira[1]]
    
    queue = deque([[inicio]]) 

    visited = []   

    while queue:
        path = queue.popleft() 
        
        atual = path[-1]      

        if atual == objetivo:
            return path 

        if atual not in visited:
            visited.append(atual)
            
            vizinhos = [
                [atual[0]-1, atual[1]],   # Cima
                [atual[0]+1, atual[1]],   # Baixo
                [atual[0], atual[1]-1],   # Esquerda
                [atual[0], atual[1]+1],   # Direita
                [atual[0]-1, atual[1]-1], # Diagonal
                [atual[0]-1, atual[1]+1], # Diagonal
                [atual[0]+1, atual[1]-1], # Diagonal
                [atual[0]+1, atual[1]+1]  # Diagonal
            ]

            for neighbor in vizinhos:
                if neighbor[0] >= 0 and neighbor[0] <= 2 and neighbor[1] >= 0 and neighbor[1] <= 2:
                    novo_caminho = path + [neighbor]
                    queue.append(novo_caminho)
                    
    return None

posicao_robo = (0, 0) 
print("Robô começou em:", posicao_robo)

destino = lerSensor(posicao_robo)

if destino != posicao_robo:
    caminho_completo = pensar(posicao_robo, destino)
    
    print("\n--- CAMINHO ENCONTRADO ---")
    print(caminho_completo) 
    
    print("\n--- SIMULANDO O MOVIMENTO ---")

    for passo in caminho_completo:
        print("O robô moveu para:", passo)
        
    print("Limpeza realizada!")

    ambiente[destino[0]][destino[1]] = 0
    
else:
    print("O ambiente já está limpo ou o robô já está no local.")