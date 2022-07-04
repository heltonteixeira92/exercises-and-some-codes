'''Problema:    1050 - DDD
Resposta:    Accepted
Linguagem:    Python 3.8 (Python 3.8.2) [+1s]
Tempo:    0.170s
Tamanho:    394 Bytes
Memória:    -
Code Golf:    0 caracteres (-616 que a mediana)
Submissão:    23/06/2021 02:21:57'''

ddd = int(input())

if ddd == 61:
    print('Brasilia')
elif ddd == 71:
    print('Salvador')
elif ddd == 11:
    print('Sao Paulo')
elif ddd == 21:
    print('Rio de Janeiro')
elif ddd == 32:
    print('Juiz de Fora')
elif ddd == 19:
    print('Campinas')
elif ddd == 27:
    print('Vitoria')
elif ddd == 31:
    print('Belo Horizonte')
else:
    print('DDD nao cadastrado')