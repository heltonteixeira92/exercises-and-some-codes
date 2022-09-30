"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

fahrenheit = float(input('Digite um valor de grau fahrenheit: '))

celsius = (fahrenheit-32) * 5 / 9

print(f'{fahrenheit}º F equivale a {celsius}º C')
