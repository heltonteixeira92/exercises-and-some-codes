def average(array):
    my_set = set(array)
    length = len(my_set)
    return sum(my_set) / length


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
