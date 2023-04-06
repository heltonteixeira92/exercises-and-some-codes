# regular function
def multiply_by_2(x):
    return x * 2


# lambda function
result = lambda x: x * 2
print(result(10))

#
concatena = lambda a, b: a + b
print(concatena('hello', ' word'))


# python program to find a+b whole square using lambda
square = lambda a, b: a ** 2 + b ** 2 + 2 * (a + b)
print(square(2, 5))

input_list = [2, 3, 4, 5, 6, 7]

# using map function to square each list item
map_answer = map(lambda x: x * x, input_list)
print(list(map_answer))

# using filter function to filter list item with value less than 5
filter_answer = filter(lambda x: x < 5, input_list)
print(list(filter_answer))

from functools import reduce

# using reduce function to sum all the list items.
reduce_answer = reduce(lambda x, y: x + y, input_list)
print(reduce_answer)
