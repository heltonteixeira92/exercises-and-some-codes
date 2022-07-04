'''Problema:    1142 - PUM
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.155s
Tamanho:    233 Bytes
Memória:    -
Submissão:    05/07/2021 20:19:10'''

n = int(input())
count = 0
num = 1
for i in range(1, n+1):
    if n != count:
        num1 = num
        num2 = num+1
        num3 = num+2
        num = num3+2
        print(f'{num1} {num2} {num3} PUM')
        count += 1
