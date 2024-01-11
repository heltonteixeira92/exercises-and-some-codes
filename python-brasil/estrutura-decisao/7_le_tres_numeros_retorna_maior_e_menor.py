"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

num1 = int(input('número um: '))
num2 = int(input('número dois: '))
num3 = int(input('número três: '))

num_list = [num1, num2, num3]

# solution

maxx = minn = num_list[0]
for elemento in num_list:
    if elemento > maxx:
        maxx = elemento

    if elemento < minn:
        minn = elemento
print(f'maior valor encontrado: {maxx}')
print(f'menor valor encontrado: {minn}')

# alternative 1 (using max and min built in)

print(f'maior número: {max(num_list)} \n menor número: {min(num_list)}')

# alternative 2 (using sort)

num_list.sort()
print(f'maior valor encontrado: {num_list[-1]}')
print(f'menor valor encontrado: {num_list[0]}')
