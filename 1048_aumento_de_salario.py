'''Problema:    1048 - Aumento de Salário
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.105s
Tamanho:    694 Bytes
Memória:    -
Submissão:    26/06/2021 16:55:58'''

# Leia o salário do funcionário e calcule e mostre o novo salário,
# bem como o valor de reajuste ganho e o índice reajustado, em percentual.

salario = float(input())
percentual = 0
salario_reajustado = 0
reajuste = 0

if salario >0 and salario <= 400.00:
    percentual = 0.15
elif salario >= 400.01 and salario <=800.00:
    percentual = 0.12
elif salario >= 800.01 and salario <=1200.00:
    percentual = 0.10
elif salario >= 1200.01 and salario <= 2000.00:
    percentual = 0.07
elif salario > 2000.00:
    percentual = 0.04
else:
    print('Valor invalido')
reajuste = salario * percentual
salario_reajustado = salario + reajuste

percentual_round = round(percentual * 100)
print('Novo salario: %.2f' % salario_reajustado)
print('Reajuste ganho: %.2f'% reajuste)
print(f'Em percentual: {percentual_round} %')
