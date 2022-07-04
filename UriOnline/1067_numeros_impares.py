'''Problema:    1067 - Números Ímpares
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.035s
Tamanho:    95 Bytes
Memória:    -
Submissão:    21/06/2021 20:28:40
'''

# números impares do 1 até o valor do imput digitado.
x = int(input())

for number in range(1, x+1):
    if number % 2 != 0:
        print(number)