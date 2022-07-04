'''Problema:    1037 - Intervalo
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.002s
Tamanho:    350 Bytes
Memória:    -
Submissão:    05/07/2021 00:19:58
'''

valor = float(input())

if valor >= 0 and valor <= 25.00:
    print('Intervalo [0,25]')
elif valor >= 25.00 and valor <= 50.00:
    print('Intervalo (25,50]')
elif valor >= 50.00 and valor <= 75.00:
    print('Intervalo (50,75]')
elif valor >= 75.00 and valor <= 100.00:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
'''
intervalo1
intervalo2
intervalo3
intervalo4
'''
