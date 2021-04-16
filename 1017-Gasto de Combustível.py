'''
Problema:    1017 - Gasto de Combustível
Resposta:    Accepted
Linguagem:    Python 3.4 (Python 3.4.3) [+1s]
Tempo:    0.030s
Tamanho:    133 Bytes
Memória:    -
Submissão:    16/04/2021 11:29:30
'''
tempo = int(input())
velocidade = int(input())

distancia = tempo * velocidade

litros = distancia / 12

print('%.3f' %litros)