x = int(input())
y = int(input())


for i in range(x+2, y-1):
    if i % 5 == 3 or i % 5 == 2:
        print(i)
