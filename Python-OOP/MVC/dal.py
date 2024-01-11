from model import Pessoa


class PessoaDal:

    @classmethod
    # o tipo de dado tem que ser uma instancia da class Pessoa
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'w') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)

    @classmethod
    def ler(cls):
        nome = 'caio'
        idade = 20
        cpf = '102548'
        return Pessoa(nome, idade, cpf)


p1 = Pessoa('caio', 20, '123465')
# PessoaDal.salvar(p1)
print(PessoaDal.ler().nome)
