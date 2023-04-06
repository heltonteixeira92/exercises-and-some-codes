entrada = int(input())
ano = mes = dia = 0

while entrada > 0:
    if entrada >= 365:
        entrada -= 365
        ano += 1
    elif 30 <= entrada < 365:
        entrada -= 30
        mes += 1
    elif entrada < 30:
        dia = entrada
        entrada -= entrada

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')
