"""
PROBLEMA: 2862 - Inseto!
RESPOSTA: Accepted
LINGUAGEM: Python 3.9 (Python 3.9.4) [+1s] {beta}
TEMPO: 0.107s
TAMANHO: 172 Bytes
MEMÓRIA: -
SUBMISSÃO: 30/05/2022 11:42:53
"""

C = int(input())

for i in range(0, C):
    power = int(input())
    if power <= 8000:
        print('Inseto!')
    elif power > 8000:
        print('Mais de 8000!')
