def listar_nomes_personagens(dados):
    lista = []
    for item in dados:
        if not isinstance(item, dict):
            raise AttributeError("Item não é dicionário")
        lista.append(item.get("name"))
    return lista


if __name__ == "__main__":
    import pickle
    with open("exercicio04.bin", "rb") as arquivo:
        dados = pickle.load(arquivo)
    print(listar_nomes_personagens(dados))
