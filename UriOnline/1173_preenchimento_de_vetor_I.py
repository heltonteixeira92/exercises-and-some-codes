'''Problema:    1173 - Preenchimento de Vetor I
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.023s
Tamanho:    139 Bytes
Memória:    -
Submissão:    20/08/2021 12:54:49 '''
# Para cada posição do vetor, escreva "N[i] = X", onde i é a posição do vetor e X é o valor armazenado na posição i
n = int(input())

for i in range(0, 10):
    print(f'N[{i}] = {n}')
    if n == 1:
        n += 1
    elif n > 1:
        n += n

