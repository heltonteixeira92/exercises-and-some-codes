'''Problema:    1002 - Área do Círculo
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.090s
Tamanho:    89 Bytes
Memória:    -
Submissão:    11/07/2021 23:52:12'''
# A fórmula para calcular a área de uma circunferência é: area = π . raio2.
# Considerando para este problema que (pi) π = 3.14159:

# Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

n = 3.14159

raio = float(input())

area = (raio * raio) * n

print('A=%.4f' %area)