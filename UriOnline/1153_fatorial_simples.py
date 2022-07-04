'''Problema:    1153 - Fatorial Simples
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.017s
Tamanho:    141 Bytes
Memória:    -
Submissão:    03/09/2021 09:44:53'''
# fatorial, ex 4! = 4.3.2.1 = 24
fatorial = int(input())
y = 0
for i in range(fatorial, 0, -1):
    if i == fatorial:
        y = i
    else:
        y *= i

print(y)


