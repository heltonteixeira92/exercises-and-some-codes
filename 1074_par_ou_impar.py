'''Problema:    1074 - Par ou Ímpar
Resposta:    Accepted
Linguagem:    Python 3.8 (Python 3.8.2) [+1s]
Tempo:    0.014s
Tamanho:    409 Bytes
Memória:    -
Submissão:    18/08/2021 15:55:57 '''
# o primeiro input é a quatidade de números que queremos colocar,
# os outros input tem retorno se o num é par,impar,positivo,negativo ou zero.
n = int(input())
count = 1

while count <= n:
    count += 1
    num = int(input())
    if num == 0:
        print('NULL')
    elif num % 2 == 0:
        if num > 0:
            print('EVEN POSITIVE')
        elif num < 0:
            print('EVEN NEGATIVE')
    elif num % 2 != 0:
        if num > 0:
            print('ODD POSITIVE')
        elif num < 0:
            print('ODD NEGATIVE')
