"""
https://docs.python.org/3/library/string.html
"""


def print_formatted(number):
    n = len(f'{number:b}')
    for i in range(1, number + 1):
        print(f'{i:>{n}d} {i:>{n}o} {i:>{n}X} {i:>{n}b}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
