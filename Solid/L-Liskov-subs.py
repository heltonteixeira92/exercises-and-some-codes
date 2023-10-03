class PessoaA:

    def se_apresentar(self):
        print('Ola, sou a pessoa A')


class PessoaB(PessoaA):
    def __init__(self):
        super().__init__()

    def se_apresetar(self):
        print('estou alterando esse metodo')


pessoa = PessoaA()
pessoa.se_apresentar()

