"""
Write a python program to check a give list of integers where the sum of the fist i integers is i.
"""


# Solution 1 -> using the 'if' statement
def check_list(nums):
    if sum(nums) != len(nums):
        return False

    return True


list1 = [1, 1, 1, 1]
list2 = [1, 2, 3, 4]

print(check_list(list1))
# True
print(check_list(list2))
# False


# Solution 2 -> using the 'if' statement
def check_list2(nums):
    return all([sum(nums) == len(nums)])


print(check_list2(list1))
# True
print(check_list2(list2))
# False
