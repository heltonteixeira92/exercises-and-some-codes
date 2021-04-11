'''
Problema:    1009 - Salário com Bônus
Resposta:    Accepted
Linguagem:    Python 3.4 (Python 3.4.3) [+1s]
Tempo:    0.043s
Tamanho:    277 Bytes
Memória:    -
Submissão:    08/04/2021 11:13:44
'''

name = str(input())
fixo = float(input())
vendas = float(input())

comissao = vendas * 0.15
total = fixo + comissao

print('TOTAL = R$ %.2f' %total)