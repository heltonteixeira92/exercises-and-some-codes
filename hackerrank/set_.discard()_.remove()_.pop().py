n = int(input())

s = set(map(int, input().split()))

N = int(input())

for i in range(N):
    entry = input().split()
    try:
        command = eval(f's.{entry[0]}({int(entry[1])})')
    except IndexError:
        command = eval(f's.{entry[0]}()')


print(sum(s))
