# ============================================================
# EXEMPLO DIDÁTICO: BAG OF WORDS BINÁRIO E DISTÂNCIA EUCLIDIANA
# ============================================================

import math

# ------------------------------------------------------------
# 1. TEXTO BASE
# ------------------------------------------------------------
print("--- ETAPA 1: CRIAÇÃO DO VOCABULÁRIO ---")
print("Digite o texto base que servirá para criar o vocabulário:")
texto = input()

# ------------------------------------------------------------
# 2. CONSTRUÇÃO DO VOCABULÁRIO
# ------------------------------------------------------------

texto_minusculo = texto.lower()
lista_palavras = texto_minusculo.split()

vocabulario = []

for palavra in lista_palavras:
    if palavra not in vocabulario:
        vocabulario.append(palavra)

vocabulario.sort()

print("\nVocabulário construído:")
print(vocabulario)
print("Tamanho do vocabulário:", len(vocabulario))

# ------------------------------------------------------------
# 3. MAPEAMENTO: PALAVRA -> POSIÇÃO NO VETOR
# ------------------------------------------------------------

indice_palavra = {}
posicao = 0
for palavra in vocabulario:
    indice_palavra[palavra] = posicao
    posicao = posicao + 1

# ------------------------------------------------------------
# 4. FRASES DE ENTRADA
# ------------------------------------------------------------

frases = []

print("\n--- ETAPA 2: LEITURA DAS 5 FRASES ---")
print("Digite 5 frases (tente usar palavras que existam no vocabulário acima):")

contador_entrada = 0
while contador_entrada < 5:
    print("Digite a frase", contador_entrada + 1, ":")
    frase_digitada = input()
    frases.append(frase_digitada)
    contador_entrada = contador_entrada + 1

# ------------------------------------------------------------
# 5. FUNÇÃO PARA CRIAR VETOR
# ------------------------------------------------------------

def criar_vetor(frase, vocabulario, indice_palavra):
    vetor = []
    tamanho_vocabulario = len(vocabulario)

    i = 0
    while i < tamanho_vocabulario:
        vetor.append(0)
        i = i + 1

    frase_minuscula = frase.lower()
    palavras_frase = frase_minuscula.split()

    for palavra in palavras_frase:
        if palavra in indice_palavra:
            pos = indice_palavra[palavra]
            vetor[pos] = 1
            
    return vetor

# ------------------------------------------------------------
# 6. CRIAÇÃO DOS VETORES DAS FRASES
# ------------------------------------------------------------

vetores = []

for frase in frases:
    vetor = criar_vetor(frase, vocabulario, indice_palavra)
    vetores.append(vetor)

print("Vetores das frases:")
i = 1
for vetor in vetores:
    print(f"Frase {i}: {vetor}")
    i = i + 1

# ------------------------------------------------------------
# 7. FUNÇÃO PARA CALCULAR DISTÂNCIA EUCLIDIANA
# ------------------------------------------------------------

def distancia_euclidiana(vetor1, vetor2):
    soma = 0
    tamanho = len(vetor1)

    indice = 0

    while indice < tamanho:
        diferenca = vetor1[indice] - vetor2[indice]
        soma = soma + (diferenca * diferenca)
        indice = indice + 1

    distancia = math.sqrt(soma)
    return distancia

# ------------------------------------------------------------
# 8. MATRIZ DE DISTÂNCIAS (5 x 5)
# ------------------------------------------------------------

print("Matriz de distâncias euclidianas (Similaridade entre as 5 frases):")
print("(Valores menores indicam maior similaridade)")
print()

linha = 0
while linha < 5:
    coluna = 0
    while coluna < 5:
        d = distancia_euclidiana(vetores[linha], vetores[coluna])
        print("{:.2f}".format(d), end="\t")
        coluna = coluna + 1
    print()
    linha = linha + 1