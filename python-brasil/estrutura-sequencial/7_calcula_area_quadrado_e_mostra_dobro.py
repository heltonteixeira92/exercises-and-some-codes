"""Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
Formula: A = b. h
b: lados, h = altura

ex1: quadrado medindo 10 cm cada de um seus lado.
    A = 10cm . 10cm
    A = 100 cm²
    ou
    A = (10cm)² = 100cm²
"""


altura = int(input('Digite a medida em cm do lado do quadrado: '))

A = altura * altura

print(f'A = {A} cm²')
