"""Errors detected during execution are called exceptions."""

T = int(input())

while T != 0:
    T -= 1

    a, b = input().split()

    try:
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print('Error Code:', e)
