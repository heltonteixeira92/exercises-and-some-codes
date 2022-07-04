'''
Problema:   1006 - Média 2
Resposta:    Accepted
Linguagem:    Python 3.4 (Python 3.4.3) [+1s]
Tempo:    0.025s
Tamanho:    262 Bytes
Memória:    -
Submissão:    07/04/2021 15:15:26
'''

A = float(input())
B = float(input())
C = float(input())

SOMA = (A*2 + B*3 + C*5)
MEDIA = float(SOMA/10)

print(SOMA)
print('MEDIA = %.1f' %MEDIA)
