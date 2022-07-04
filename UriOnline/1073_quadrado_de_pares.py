'''Problema:    1073 - Quadrado de Pares
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.157s
Tamanho:    152 Bytes
Memória:    -
Submissão:    03/07/2021 15:08:54 '''

# Apresente o quadrado de cada um dos valores pares, de 1 até n
n = int(input())

for number in range(1, n+1):
    if number % 2 == 0:
        square = number * number
        print(f'{number}^2 = {square}')