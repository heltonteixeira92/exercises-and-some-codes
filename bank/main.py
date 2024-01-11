class Animal:
    def andar(self):
        print('estou andando como um animal')

    def correr(self):
        print('estou correndo')

    def pular(self):
        print('estou correndo')


class Felino():

    def felino(self):
        print('eu sou um felino')

    def correr(self):
        print('felino correndo')


class Gato(Felino, Animal):

    def mia(self):
        print('eu estou miando')


gato = Gato()
gato.correr()
gato.felino()
gato.mia()