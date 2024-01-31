"""https://docs.python.org/3/tutorial/datastructures.html#sets"""

n = int(input())
en_students = set(map(int, input().split()))
b = int(input())
fr_students = map(int, input().split())
# a | b or a.union(b)

one_subscription = en_students.union(fr_students)
print(len(one_subscription))
