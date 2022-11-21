""""
passo a passo para saber se um ano é ou não bissexto.
Passo 1) Verificar se o ano é divisível por 4.

– Se não for divisível por 4, então, não é ano bissexto.

– Se for divisível por 4, então, vamos para o passo 2.
Passo 2) Verificar se o ano é divisível por 100.

– Se não for divisível por 100, então, é ano bissexto (caso 1).

– Se for divisível por 100, vamos para o passo 3.
Passo 3) Verificar se o ano é divisível por 400.

– Se não for divisível por 400, então, o ano não é bissexto.

– Se for divisível por 400, então, é ano bissexto (caso 2).

>>> is_leap(1990)
False

>>> is_leap(1900)
False

>>> is_leap(2100)
False

>>> is_leap(2000)
True

>>> is_leap(2400)
True

"""


def is_leap(year):
    leap = False

    # Write your logic here

    if year % 4 == 0:
        if year % 100 != 0:
            leap = True

        if year % 400 == 0:
            leap = True

    else:
        leap = False

    return leap

