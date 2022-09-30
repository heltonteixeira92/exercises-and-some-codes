""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês

dica: Para saber quanto o funcionário ganha por hora, basta dividir o salário dele por 220 horas que é sua carga horária mensal:
44horas semanais x 5 semanas = 220.
"""
salario = float(input('Digite seu salário:'))

valor_hora = salario / 220

print(f'Você ganha R${valor_hora:.2f} por hora')
