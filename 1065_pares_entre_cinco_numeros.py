'''
Problema:    1065 - Pares entre Cinco Números
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.085s
Tamanho:    208 Bytes
Memória:    -
Submissão:    29/06/2021 23:46:59 '''

count = 1
lista = []
while count <= 5:
    lista.append(input())
    count += 1

count_par = 0
for i in lista:
    if int(i) % 2 == 0:
        count_par += 1


print(f'{count_par} valores pares')

