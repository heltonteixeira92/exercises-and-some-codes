"""Crie uma função que receba uma lista com dados numéricos e strings de números misturados.
Retorne ela ordenada de forma decrescente considerando as strings como valores numéricos.
Retorne também o menor e o maior valor da lista.
Considere a melhor performance em sua solução.

𝑙𝑖𝑠𝑡𝑎 = [9, 2, 95, 28, 0, 73, 81, 91, 71, '22', 6, 21, 1, 47, "52", 35, 68, 29, 66, 91, 81, "99", 40]
"""


lista = [9, 2, 95, 28, 0, 73, 81, 91, 71, '22', 6, 21, 1, 47, "52", 35, 68, 29, 66, 91, 81, "99", 40]
lista.sort(reverse=True, key=int)
print(lista)
print(f'Maior valor: {max(lista, key=int)}\nMenor valor: {min(lista, key=int)}')
