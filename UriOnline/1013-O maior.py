'''

Problema:    1013 - O Maior
Resposta:    Accepted
Linguagem:    Python 3.4 (Python 3.4.3) [+1s]
Tempo:    0.041s
Tamanho:    376 Bytes
Memória:    -
Submissão:    11/04/2021 12:24:46
'''

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a >= b and a >= c:
    print('{} eh o maior'.format(a))
elif b >= a and b >= c:
    print('{} eh o maior'.format(b))
elif c >= a and c >= b:
    print('{} eh o maior'.format(c))
