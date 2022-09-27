""" Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. """

sexo = input('Digite seu sexo (M ou F): ').upper()

if sexo == 'M':
    print('MASCULINO')
elif sexo == 'F':
    print('FEMININO')
else:
    print('SEXO INVÁLIDO')
