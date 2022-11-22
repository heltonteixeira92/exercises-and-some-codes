"""
exemplo de uso do map

o map basicamente é uma forma de aplicar a mesma função em diferentes números

kmh = kilometros por hora
mph = milhas por hora
"""

mph = []
kmh = [10, 20, 30, 40, 60, 50, 65, 89, 63]

# using for
for i in kmh:
    mph.append(i/1.61)

print(mph)

# using map(func, iterables)
mph2 = list(map(lambda x: x/1.61, kmh))

print(mph2)
