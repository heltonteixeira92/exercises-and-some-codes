"""Problema:    1042 - Sort Simples
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.039s
Tamanho:    214 Bytes
Memória:    -
Submissão:    25/06/2021 01:13:45
"""
a, b, c = input().split()

lista_original = [int(a), int(b), int(c)]
lista_ordenada = sorted(lista_original)


for num in lista_ordenada:
    print(num)
print('')
for num in lista_original:
    print(num)