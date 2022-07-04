'''Problema:    1143 - Quadrado e ao Cubo
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.009s
Tamanho:    236 Bytes
Memória:    -
Submissão:    29/07/2021 23:28:21 '''


def quadrado_e_ao_cubo(qtd_saida):
    for i in range(1, qtd_saida+1):
        multi = i
        print(i, end=' ')
        i *= i
        print(i, end=' ')
        i *= multi
        print(i)


quadrado_e_ao_cubo(int(input()))