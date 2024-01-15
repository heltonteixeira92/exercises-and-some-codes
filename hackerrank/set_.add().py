N = int(input())

count = 0
s = set()

while count < N:
    count += 1
    s.add(str(input()))

print(len(s))
