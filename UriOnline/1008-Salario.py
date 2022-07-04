'''
Problema:    1008 - Salário
Resposta:    Accepted
Linguagem:    Python 3.8 (Python 3.8.2) [+1s] {beta}
Tempo:    0.234s
Tamanho:    314 Bytes
Memória:    -
Submissão:    02/04/2021 16:22:17
'''

NUMBER = int(input())
QUANT_HORAS_TRAB = int(input())
VALORHORA = float(input())

SALARY = QUANT_HORAS_TRAB * VALORHORA

print(f'NUMBER = {NUMBER}')
print(f'SALARY = U$ {SALARY:.2f}')