'''Problema:    1049 - Animal
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.000s
Tamanho:    764 Bytes
Memória:    -
Submissão:    03/07/2021 15:31:31 '''

nive1 = str(input())
nivel2 = str(input())
nivel3 = str(input())


if nive1 == 'vertebrado':
    if nivel2 == 'ave':
        if nivel3 == 'carnivoro':
            print('aguia')
        elif nivel3 == 'onivoro':
            print('pomba')
    elif nivel2 == 'mamifero':
        if nivel3 == 'onivoro':
            print('homem')
        elif nivel3 == 'herbivoro':
            print('vaca')
elif nive1 == 'invertebrado':
    if nivel2 == 'inseto':
        if nivel3 == 'hematofago':
            print('pulga')
        elif nivel3 == 'herbivoro':
            print('lagarta')
    elif nivel2 == 'anelideo':
        if nivel3 == 'hematofago':
            print('sanguessuga')
        elif nivel3 == 'onivoro':
            print('minhoca')
