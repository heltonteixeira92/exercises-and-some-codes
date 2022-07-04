'''Problema:
    1117 - Validação de Nota
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.065s
Tamanho:    248 Bytes
Memória:    -
Submissão:    11/07/2021 23:28:41 '''

count = 1
soma = 0
while count <= 2:
    entrada = float(input(''))
    if entrada >= 0 and entrada <= 10:
        soma += entrada
        count += 1
    else:
        print('nota invalida')

media = soma / 2
print('media = %.2f' %media)