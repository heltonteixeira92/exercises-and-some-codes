lista = []
contador = 0

while contador < 5:
    try:
        n = float(input('Digite um número: '))
        lista.append(n)
        contador += 1

    except ValueError:
        print('Apenas números são permitidos')

print(lista)
