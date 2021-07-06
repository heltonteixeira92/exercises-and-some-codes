'''Problema:    1080 - Maior e Posição
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.047s
Tamanho:    187 Bytes
Memória:    -
Submissão:    05/07/2021 00:15:30 '''

cont = 1
lista_num = []
while cont <= 100:
    lista_num.append(int(input()))
    cont += 1


maior = max(lista_num)
print(maior)
indice = lista_num.index(maior)
print(indice+1)