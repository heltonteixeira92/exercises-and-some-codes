'''Problema:    1040 - Média 3
Resposta:    Accepted
Linguagem:    Python 3.9 (Python 3.9.4) [+1s] {beta}
Tempo:    0.017s
Tamanho:    634 Bytes
Memória:    -
Submissão:    21/06/2021 20:04:28
'''

# Calcula a média de 4 valores com pesos.

a, b, c, d = input().split()

a = float(a)
b = float(b)
c = float(c)
d = float(d)

a = a*2
b = b*3
c = c*4
d = d*1

soma = a+b+c+d
media = soma/10
print('Media: %.1f' %media)

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif media >= 5.0 and media <= 6.9:
    print('Aluno em exame.')
    e = float(input())
    media = (media + e)/2
    print('Nota do exame: %.1f' % e)
    if media >= 5.0:
        print('Aluno aprovado.')
        print('Media final: %.1f' % media)
    else:
        print('Aluno reprovado.')
        print('Media final: %.1f' % media)