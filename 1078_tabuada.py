'''Problema:    1078 - Tabuada
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.301s
Tamanho:    100 Bytes
Memória:    -
Submissão:    29/06/2021 22:20:42'''

N = int(input())

for i in range(1, 11):
    result = i * N
    print(f'{i} x {N} = {result}')
