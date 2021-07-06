'''Problema:    1114 - Senha Fixa
Resposta:    Accepted
Linguagem:    Python 3.8 (Python 3.8.2) [+1s]
Tempo:    0.140s
Tamanho:    175 Bytes
Memória:    -
Submissão:    05/07/2021 23:03:45 '''

senha = 2002
while senha:
    entrada = int(input())
    if entrada == senha:
        print('Acesso Permitido')
        break;
    else:
        print('Senha Invalida')