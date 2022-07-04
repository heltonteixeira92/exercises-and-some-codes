'''

Problema:    1015 - Distância Entre Dois Pontos
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.075s
Tamanho:    194 Bytes
Memória:    -
Submissão:    16/04/2021 16:11:04
'''

x1, y1 = input().split()
x2, y2 = input().split()

x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

distancia = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

print('%.4f' %distancia)