#https://www.youtube.com/watch?v=TgdnbnmT44s  resposta melhor

dias = int(input())
ano = 0
mes = 0


if dias >= 365 and dias <= 729:
    ano += 1
    dias -= 365
elif dias >= 730:
    ano += 2
    dias -= 730
    
if dias >= 30 and dias <= 59:
    mes += 1
    dias -=  30
elif dias >= 60 and dias <= 89:
    mes += 2
    dias -= 60
elif dias == 90:
    mes += 3
elif dias == 120:
    mes += 4

if dias <= 29:
    dias = dias

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dias} dia(s)')
