"""A pesquisa binário sempre vai começar a busca pela metade da lista,
ela validar se o valor está está procurando está a em uma escala maior ou menor,
assim descartando as possibilidades fora do range. A lista tem que ser sempre ordenada."""


def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    # step = 0

    while baixo <= alto:
        # step += 1
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
            # return print(f'O objeto se encontra no index {meio} da lista, percorremos a lista {step}x para encontra-lo.')
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


minha_lista = [1, 3, 5, 7, 9]

pesquisa_binaria(minha_lista, 1)

