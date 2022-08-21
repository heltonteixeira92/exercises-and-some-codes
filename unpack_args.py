full_name = ['Helton', 'Teixeira', 'de', 'Souza']

# the args name is a conversion, I can call it anything, important is has * (asterisk)

first_name, middle_name, *rest = full_name

print(first_name, middle_name)
# > Helton Teixeira

print(*rest)
# > de Souza


# we can use *range to create a list of numbers
list_generated = [*range(1, 11)]
# > [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
