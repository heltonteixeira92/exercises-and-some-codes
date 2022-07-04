'''Problema:    1180 - Menor e Posição
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.018s
Tamanho:    163 Bytes
Memória:    -
Submissão:    18/08/2021 15:04:14 '''
# o programa pega varios valores e retorno o menor e sua posicão
n = int(input())
lista = [int(x) for x in input().split()]
menor = min(lista)
pos = lista.index(menor)
print(f'Menor valor: {menor}')
print(f'Posicao: {pos}')
