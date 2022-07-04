"""
PROBLEMA: 1066 - Pares, Ímpares, Positivos e Negativos
RESPOSTA: Accepted
LINGUAGEM: Python 3.9 (Python 3.9.4) [+1s] {beta}
TEMPO: 0.067s
TAMANHO: 468 Bytes
MEMÓRIA: -
SUBMISSÃO: 01/06/2022 10:34:34
"""

values = []
count = 5
positive = negative = even = odd = 0

while count != 0:
    values.append(int(input()))
    count -= 1

for i in values:
    if i % 2 == 0:
        even += 1
    if i % 2 != 0:
        odd += 1
    if i < 0:
        negative += 1
    elif i > 0:
        positive += 1

print(f'{even} valor(es) par(es)')
print(f'{odd} valor(es) impar(es)')
print(f'{positive} valor(es) positivo(s)')
print(f'{negative} valor(es) negativo(s)')
