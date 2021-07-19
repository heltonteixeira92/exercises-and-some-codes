'''Problema:    1157 - Divisores I
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.007s
Tamanho:    81 Bytes
Memória:    -
Submissão:    16/07/2021 23:36:06 '''

N = int(input())

for i in range(1, N+1):
    if N % i == 0:
        print(i)