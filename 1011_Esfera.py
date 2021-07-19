'''Problema:    1011 - Esfera
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.000s
Tamanho:    116 Bytes
Memória:    -
Submissão:    19/07/2021 12:28:15'''

# calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R).
# A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o valor 3.14159.
pi = 3.14159
R = float(input())
potenciaR = R**3
volume = (4/3) * pi * potenciaR
print('VOLUME = %.3f' % volume)
