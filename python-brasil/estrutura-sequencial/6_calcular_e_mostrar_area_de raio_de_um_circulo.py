"""Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""


"""Fórmula para obter a área do círculo:

A = π · r²

π: constante Pi (3,14)
r: raio
"""

raio = float(input('Raio do círculo: '))

area = 3.14 * (raio * raio)

print('A área do círculo: {:.2f}'.format(area))
