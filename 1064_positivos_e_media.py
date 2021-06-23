'''Problema:    1064 - Positivos e Média
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.073s
Tamanho:    345 Bytes
Memória:    -
Submissão:    23/06/2021 12:38:37'''

lista_valores = []
contador = 1
valor_positivo = 0
soma = 0
while contador <= 6:
    entrada = float(input())
    lista_valores.append(entrada)
    if entrada > 0:
        soma += entrada
        valor_positivo += 1
    contador += 1
media = soma / valor_positivo
print(f'{valor_positivo} valores positivos')
print('%.1f' % media)

