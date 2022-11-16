def pesquisa_binaria(lista, item):
    """ Implementaçãa de pesquisa binária iterativamente"""
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == item:
            return meio
        elif lista[meio] > item:
            direita = meio - 1
        else: # lista[meio] < item
            esquerda = meio + 1
    return - 1


lista = [0, 10, 20, 30, 40, 50, 60, 70]
print('pesquisa com sucesso:', pesquisa_binaria(lista, 20))
