'''Problema:    1044 - Múltiplos
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.000s
Tamanho:    272 Bytes
Memória:    -
Submissão:    25/06/2021 01:32:38 '''

# Basta dividir o maior pelo menor,se a divisão for exata,eles são múltiplos entre si.

a, b = input().split()

a = int(a)
b = int(b)

if b > a:
    if b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
elif a > b:
    if a % b == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')