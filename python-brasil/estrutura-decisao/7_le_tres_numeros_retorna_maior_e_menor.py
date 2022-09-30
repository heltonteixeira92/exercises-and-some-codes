"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

num1 = int(input('número um: '))
num2 = int(input('número dois: '))
num3 = int(input('número três: '))

# solution 0
if num2 < num1 > num3:
    print(f' {num1} foi o maior número recebido.')
elif num3 < num2 > num1:
    print(f' {num2} foi o maior número recebido.')
elif num1 < num3 > num2:
    print(f' {num3} foi o maior número recebido.')