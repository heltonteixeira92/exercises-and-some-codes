entrada = int(input())
count = 0
soma = 0
while count < 5:
    if entrada == 0:
        break
    elif entrada % 2 == 0:
        soma += entrada
        entrada += 1
        count += 1
    else:
        entrada += 1

if entrada != 0:
    print(soma)

