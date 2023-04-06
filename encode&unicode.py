# """\\xC6\\xA6\\xC4\\x93\\xC2\\xA1..."""
#
#
# enconding = b'\xc6\xa6\xc4\x93\xc2\xa1\xc6\x9e\xc4\x81'
# deconding = 'Ʀē¡ƞā'
#
# print(enconding.decode('utf-8'))
# print(deconding.encode('utf-8'))

janela = 2.00 * 1.20
porta = 0.80 * 1.90

lmetragem1 = float(input('largura da parade 1: '))
hmetragem1 = float(input('comprimento da parede 1: '))

lmetragem2 = float(input('largura da parade 2: '))
hmetragem2 = float(input('comprimento da parede 2: '))

lmetragem3 = float(input('largura da parade 3: '))
hmetragem3 = float(input('comprimento da parede 3: '))

lmetragem4 = float(input('largura da parade 4: '))
hmetragem4 = float(input('comprimento da parede 4: '))

qtd_porta = int(input('quantidade de portas'))
qtd_janelas = int(input('quantidade de janelas'))


mquadrado = (lmetragem1 * hmetragem1) + (lmetragem2 * hmetragem2) + (lmetragem3 * hmetragem3) + (lmetragem4 * hmetragem4)

mquadradoj = janela * qtd_janelas
mquadradop = porta * qtd_porta

total = mquadrado - mquadradop - mquadradoj

print(mquadrado, 'm²')
print('Então a área a ser pintada é igual à {:.2f}m²'.format(total))
