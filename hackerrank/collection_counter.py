"""A counter is a container that stores elements as dictionary keys,
and their counts are stored as dictionary values.

>>> from collections import Counter
>>>
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>>
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>>
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]
"""

from collections import Counter

number_of_shoes = int(input())  # X
all_shoes_size = Counter(map(int, input().split()))  # list of shoes size

number_of_customers = int(input())  # N

purchased = []
earned = 0

for _ in range(number_of_customers):
    shoe_size_desired, price = map(int, input().split())
    if all_shoes_size[shoe_size_desired] > 0:
        earned += price
        all_shoes_size[shoe_size_desired] -= 1

print(earned)
