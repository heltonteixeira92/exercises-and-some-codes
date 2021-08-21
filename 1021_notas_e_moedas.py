# still not accepted

valor = float(input())
nota_cem = nota_cinquenta = nota_vinte = nota_dez = nota_cinco = nota_dois = 0
moeda_um = moeda_cinquenta = moeda_vinte_cinco = moeda_dez = moeda_cinco = moeda_um_centavo = 0
while valor > 0.0:
    if valor >= 100:
        valor -= 100
        nota_cem += 1
    elif valor >= 50:
        valor -= 50
        nota_cinquenta += 1
    elif valor >= 20:
        valor -= 20
        nota_vinte += 1
    elif valor >= 10:
        valor -= 10
        nota_dez += 1
    elif valor >= 5:
        valor -= 5
        nota_cinco += 1
    elif valor >= 2:
        valor -= 2
        nota_cinco += 1
    elif valor >= 1:
        valor -= 1
        moeda_um += 1
    elif valor >= 0.50:
        valor -= 0.50
        moeda_cinquenta += 1
    elif valor >= 0.25:
        valor -= 0.25
        moeda_vinte_cinco += 1
    elif valor >= 0.5:
        valor -= 0.5
        moeda_cinco += 1
    elif valor >= 0.1:
        valor -= 0.1
        moeda_um_centavo += 1


print('NOTAS:')
print(f'{nota_cem} nota(s) de R$ 100.00')
print(f'{nota_cinquenta} nota(s) de R$ 50.00')
print(f'{nota_vinte} nota(s) de R$ 20.00')
print(f'{nota_dez} nota(s) de R$ 10.00')
print(f'{nota_cinco} nota(s) de R$ 5.00')
print(f'{nota_dois} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moeda_um} nota(s) de R$ 1.00')
print(f'{moeda_cinquenta} nota(s) de R$ 0.50')
print(f'{moeda_vinte_cinco} nota(s) de R$ 0.25')
print(f'{moeda_dez} nota(s) de R$ 0.10')
print(f'{moeda_cinco} nota(s) de R$ 0.05')
print(f'{moeda_um_centavo} nota(s) de R$ 0.01')



