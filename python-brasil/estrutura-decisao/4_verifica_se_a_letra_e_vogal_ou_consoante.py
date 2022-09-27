""" Faça um Programa que verifique se uma letra digitada é vogal ou consoante. """

letra = str(input('Digite uma letra: ')).upper()[0]

vogal = 'AEIOU'
consoante = 'BCDFGJKLMNPQRSTVWXZ'

if letra in vogal:
    print(f'A letra "{letra}" , é uma vogal')
elif letra in consoante:
    print(f'A letra "{letra}" é uma consoante')
