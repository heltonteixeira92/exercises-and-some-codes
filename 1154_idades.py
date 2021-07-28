'''Problema:    1154 - Idades
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.054s
Tamanho:    181 Bytes
Memória:    -
Submissão:    28/07/2021 20:26:10 '''

cont = 0
soma = 0
while True:
    num = int(input())
    if num > 0:
        soma += num
        cont += 1
    else:
        break

media = soma/cont
print('%.2f' % media)
