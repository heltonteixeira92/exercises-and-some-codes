def pesquisa_binaria_recursiva(lista, esquerda=0, direita=None, item=None):
    """Implementando pesquisa binária recursivamente"""

    # 1. caso base: o elemento não está presente.

    if direita < esquerda:
        return -1

    meio = (esquerda + direita) // 2

    # 2. Nosso palpite estava certo: o elemento está no meio do arranjo.
    if lista[meio] == item:
        return meio

    # 3. O palpite estava errado: atualizamos os limites e continuamos a busca.
    elif lista[meio] > item:
        return pesquisa_binaria_recursiva(lista, esquerda, meio - 1, item)

    else: # lista[meio] < item
        return pesquisa_binaria_recursiva(lista, meio + 1, direita, item)


lista = [0, 10, 20, 30, 40, 50, 60, 70]

print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(lista, 0, len(lista) - 1, 50))
