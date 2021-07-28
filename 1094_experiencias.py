'''Problema:    1094 - Experiências
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.106s
Tamanho:    893 Bytes
Memória:    -
Submissão:    28/07/2021 20:04:10 '''
# Fórmula do percentual:
# p =  ( x / y ) * 100
# Onde, p = Porcentagem x = X Valor y = Y Valor

N = int(input())
count = 1
S = R = C = ''
total_sapos = total_ratos = total_coelhos = 0
lista_qtd = []
while count <= N:
    qtd, tipo = input().split()
    count += 1
    if tipo == 'C':
        total_coelhos += int(qtd)
    elif tipo == 'S':
        total_sapos += int(qtd)
    elif tipo == 'R':
        total_ratos += int(qtd)

total = total_ratos + total_sapos + total_coelhos

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {total_coelhos}')
print(f'Total de ratos: {total_ratos}')
print(f'Total de sapos: {total_sapos}')

perc_coelhos = float((total_coelhos/total) * 100)
perc_ratos = float((total_ratos/total) * 100)
perc_sapos = float((total_sapos/total) * 100)

print('Percentual de coelhos: {0:.2f} %'.format(perc_coelhos))
print('Percentual de ratos: {0:.2f} %'.format(perc_ratos))
print('Percentual de sapos: {0:.2f} %'.format(perc_sapos))
