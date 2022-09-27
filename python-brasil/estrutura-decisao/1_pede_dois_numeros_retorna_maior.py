""" Faça um Programa que peça dois números e imprima o maior deles. """

num1 = int(input('digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))

print(f'número {num1} é maior que o número {num2}') if num1 > num2 else print(f'número {num2} é maior que o número {num1}')
