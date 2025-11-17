def search_high_values(dados):
    if not isinstance(dados, list):
        raise TypeError("Entrada deve ser lista")
    lista = []
    for item in dados:
        if "high" not in item:
            raise KeyError("Campo high ausente")
        lista.append(item["high"])
    return lista


def search_low_values(dados):
    if not isinstance(dados, list):
        raise TypeError("Entrada deve ser lista")
    lista = []
    for item in dados:
        if "low" not in item:
            raise KeyError("Campo low ausente")
        lista.append(item["low"])
    return lista


if __name__ == "__main__":
    import pickle
    with open("exercicio03.bin", "rb") as arquivo:
        dados = pickle.load(arquivo)
    print(search_high_values(dados))
    print(search_low_values(dados))
