"""
PROBLEMA: 1046 - Tempo de Jogo
RESPOSTA: Accepted
LINGUAGEM: Python 3.9 (Python 3.9.4) [+1s] {beta}
TEMPO: 0.034s
TAMANHO: 408 Bytes
MEMÓRIA: -
SUBMISSÃO: 23/03/2023 11:17:52
"""

start_hour, finish_hour = input().split()

start_hour, finish_hour = int(start_hour), int(finish_hour)

if start_hour > finish_hour:
    time = 24 - (start_hour - finish_hour)
    print(f'O JOGO DUROU {time} HORA(S)')
elif finish_hour > start_hour:
    time = finish_hour - start_hour
    print(f'O JOGO DUROU {time} HORA(S)')
else:
    print(f'O JOGO DUROU 24 HORA(S)')
