'''Problema:    1134 - Tipo de Combustível
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.000s
Tamanho:    394 Bytes
Memória:    -
Submissão:    29/07/2021 23:43:22'''
# Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código
# (até que seja válido). O programa será encerrado quando o código informado for o número 4.
alcool = gasolina = diesel = 0

while True:
    escolha = int(input())
    if escolha == 4:
        print('MUITO OBRIGADO')
        print(f'Alcool: {alcool}')
        print(f'Gasolina: {gasolina}')
        print(f'Diesel: {diesel}')
        break
    elif escolha == 1:
        alcool += 1
    elif escolha == 2:
        gasolina += 1
    elif escolha == 3:
        diesel += 1
