'''
Problema:    1035 - Teste de Seleção 1
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.033s
Tamanho:    223 Bytes
Memória:    -
Submissão:    15/05/2021 18:21:47 '''

A, B, C, D = input().split()

A = int(A)
B = int(B)
C = int(C)
D = int(D)

if B > C and D > A and C + D > A + B and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print('Valores nao aceitos')


