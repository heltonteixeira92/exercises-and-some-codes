'''
Problema: 1930 - Tomadas
Resposta: Accepted
Linguagem: Python 3.4 (Python 3.4.3) [+1s]
Tempo:   0.002s
Tamanho:    275 Bytes
Memória:    -
Submissão:    02/04/2021 16:11:44 '''

# pega 4 valores na mesma linha e atribui a variáveis
T1, T2, T3, T4 = input().split(" ")

# converto o valor para o tipo necessário
T1 = int(T1)
T2 = int(T2)
T3 = int(T3)
T4 = int(T4)

Tomadas = (T1+T2+T3+T4 - 3)

print('{}'.format(Tomadas))
