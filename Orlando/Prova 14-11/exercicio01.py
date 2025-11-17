def extrair_dados(dados):
    if "results" not in dados:
        raise KeyError("'results' não encontrado no dicionário de entrada")

    resultados = dados["results"]

    if not isinstance(resultados, list):
        raise TypeError("'results' deve ser uma lista")

    lista_final = []

    for personagem in resultados:
        obrigatorios = ("id", "name", "species", "gender")
        if not isinstance(personagem, dict):
            raise TypeError("Cada item em 'results' deve ser um dicionário")
        for chave in obrigatorios:
            if chave not in personagem:
                raise KeyError(f"Campo obrigatório ausente: {chave}")

        novo = {
            "id": personagem["id"],
            "nome": personagem["name"],
            "especie": personagem["species"],
            "genero": personagem["gender"]
        }
        lista_final.append(novo)

    return lista_final


if __name__ == "__main__":
    import pickle
    with open("exercicio01.bin", "rb") as arquivo:
        dados_rickandmortyapi = pickle.load(arquivo)
    print(extrair_dados(dados_rickandmortyapi))
