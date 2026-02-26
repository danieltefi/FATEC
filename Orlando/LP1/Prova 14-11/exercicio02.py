def extrair_dados(lista_enderecos):
    if not isinstance(lista_enderecos, list):
        raise TypeError("Entrada deve ser uma lista")

    lista_final = []

    for item in lista_enderecos:
        obrigatorios = ("cep", "localidade", "estado")

        if not isinstance(item, dict):
            raise TypeError("Cada item deve ser um dicionário")

        for chave in obrigatorios:
            if chave not in item:
                raise KeyError(f"Campo obrigatório ausente: {chave}")

        tupla = (item["cep"], item["localidade"], item["estado"])
        lista_final.append(tupla)

    return lista_final


if __name__ == "__main__":
    import pickle
    with open("exercicio02.bin", "rb") as arquivo:
        dados = pickle.load(arquivo)
    print(extrair_dados(dados))
