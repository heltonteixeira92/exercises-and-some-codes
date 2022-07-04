"""
PROBLEMA: 1116 - Dividindo X por Y
RESPOSTA: Accepted
LINGUAGEM: Python 3.9 (Python 3.9.4) [+1s] {beta}
TEMPO: 0.301s
TAMANHO: 187 Bytes
MEMÓRIA: -
SUBMISSÃO: 01/06/2022 10:12:08
"""

entry = int(input())

for i in range(0, entry):
    X, Y = input().split()
    try:
        print(int(X)/int(Y))

    except ZeroDivisionError:
        print('divisao impossivel')
