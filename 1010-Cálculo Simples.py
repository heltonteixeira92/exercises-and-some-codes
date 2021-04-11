'''

Problema:    1010 - Cálculo Simples
Resposta:    Accepted
Linguagem:    Python 3.4 (Python 3.4.3) [+1s]
Tempo:    0.031s
Tamanho:    385 Bytes
Memória:    -
Submissão:    11/04/2021 11:29:42
'''
valor1 = input().split()
valor2 = input().split()
a, b, c = valor1
x, y, w = valor2

y, w = int(y), float(w)
b, c = int(b), float(c)

multi2 = b * c
multi1 = y * w

total = multi2 + multi1
total = float(total)

print('VALOR A PAGAR: R$ %.2f' %total)