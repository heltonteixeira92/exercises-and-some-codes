""" Faça um Programa que peça um valor e mostr8e na tela se o valor é positivo ou negativo. """

num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'{num} é um número par')
elif num % 2 != 0:
    print(f'{num} é um número impar')
else:
    print('valor inválido')
