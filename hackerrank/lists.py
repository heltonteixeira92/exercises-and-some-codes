
N = int(input())

command = ''
index = None
value = None

lista = []

while N != 0:
    N -= 1
    command, *value = input().split()

    if command == 'insert':
        lista.insert(int(value[0]), int(value[1]))
    elif command == 'remove':
        lista.remove(int(value[0]))
    elif command == 'append':
        lista.append(int(value[0]))
    elif command == 'print':
        print(lista)
    elif command == 'reverse':
        lista.reverse()
    elif command == 'pop':
        lista.pop()
    elif command == 'sort':
        lista.sort()
