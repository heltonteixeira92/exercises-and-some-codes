'''Problema:    1060 - Números Positivos
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.040s
Tamanho:    217 Bytes
Memória:    -
Submissão:    23/06/2021 02:54:12
'''

# numeros positivos
count = 1
lista = []
positivo = 0

while count <= 6:
    lista.append(float(input()))
    count += 1

for numero in lista:
    if numero > 0:
        positivo += 1

print(f'{positivo} valores positivos')
