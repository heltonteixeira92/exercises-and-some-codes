'''Problema:    1038 - Lanche
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.001s
Tamanho:    298 Bytes
Memória:    -
Submissão:    25/06/2021 02:23:10'''

# Simula a compra de produto pelo código, qtd é quatidade, o dict produtos armazena cod e valor unit.

codigo, qtd = input().split()
produtos = {'1': '4',
            '2': '4.5',
            '3': '5.0',
            '4': '2.0',
            '5': '1.5'}

for cod, valor in produtos.items():
    if cod == codigo:
        total = float(valor) * float(qtd)
        print('Total: R$ %.2f' % total)
