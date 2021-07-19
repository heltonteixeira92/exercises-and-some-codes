'''Problema:    1018 - Cédulas
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.085s
Tamanho:    906 Bytes
Memória:    -
Submissão:    19/07/2021 13:06:00'''

N = int(input())
nota_cem = 0
nota_cinquenta = 0
nota_vinte = 0
nota_dez = 0
nota_cinco = 0
nota_dois = 0
nota_um = 0

print(N)

while N > 0:
    if N >= 100:
        nota_cem += 1
        N -= 100
    elif 50 <= N < 100:
        nota_cinquenta += 1
        N -= 50
    elif 20 <= N < 50:
        nota_vinte += 1
        N -= 20
    elif 10 <= N < 20:
        nota_dez += 1
        N -= 10
    elif 5 <= N < 10:
        nota_cinco += 1
        N -= 5
    elif 2 <= N < 5:
        nota_dois += 1
        N -= 2
    elif 1 <= N < 2:
        nota_um += 1
        N -= 1


print(f'{nota_cem} nota(s) de R$ 100,00')
print(f'{nota_cinquenta} nota(s) de R$ 50,00')
print(f'{nota_vinte} nota(s) de R$ 20,00')
print(f'{nota_dez} nota(s) de R$ 10,00')
print(f'{nota_cinco} nota(s) de R$ 5,00')
print(f'{nota_dois} nota(s) de R$ 2,00')
print(f'{nota_um} nota(s) de R$ 1,00')
