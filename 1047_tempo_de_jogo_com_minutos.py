hora_ini, minuto_ini, hora_final, minuto_final = input().split()
tempo_hora = 0
tempo_min = 0
hora_ini = int(hora_ini)
hora_final = int(hora_final)
minuto_ini = int(minuto_ini)
minuto_final = int(minuto_final)


for i in range(hora_ini, hora_final):
    tempo_hora += 1

if minuto_ini < minuto_final:
    for i in range(minuto_ini, minuto_final):
        tempo_min += 1
elif minuto_ini > minuto_final:
    tempo_min = 60
    for i in range(minuto_ini, minuto_final):
        tempo_min -= 1

print(f'{tempo_hora} {tempo_min}')