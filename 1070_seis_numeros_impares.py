'''Problema:    1070 - Seis Números Ímpares
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.172s
Tamanho:    168 Bytes
Memória:    -
Submissão:    22/06/2021 12:17:00
'''

# 6 próximos números impares
X = int(input())
Count = 0
for number in range(X, X*3):
    if number % 2 != 0:
        print(number)
        Count += 1
        if Count >= 6:
            break

