'''Problema:    1019 - Conversão de Tempo
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.000s
Tamanho:    290 Bytes
Memória:    -
Submissão:    20/07/2021 12:02:25'''
#  Imprima o tempo lido no arquivo de entrada (segundos),
#  convertido para horas:minutos:segundos, conforme exemplo fornecido.
num = int(input())
hora = 0
minuto = 0
segundo = 0
while num > 0:
    if num >= 3600:
        num -= 3600
        hora += 1
    elif num >= 60:
        num -= 60
        minuto += 1
    elif num < 60:
        num -= 1
        segundo += 1

print(f'{hora}:{minuto}:{segundo}')
