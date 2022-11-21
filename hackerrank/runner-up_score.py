n = int(input())
arr = list(map(int, input().split(maxsplit=n)))

maior = max(arr)

arr2 = [i for i in arr if i != maior]

print(arr2)
seg_maior = max(arr2)

# arr = [x for x in input().split()]


