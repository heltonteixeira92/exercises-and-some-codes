'''Problema:    1075 - Resto 2
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.064s
Tamanho:    82 Bytes
Memória:    -
Submissão:    29/06/2021 22:25:09'''

N = int(input())

for i in range(1, 10001):
    if i % N == 2:
        print(i)
