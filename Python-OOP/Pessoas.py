class Pessoas:

    # atributo de classe, ou sejá algo que não é especifico de uma instancia
    #  e sim toda a classe e instancias que foram criadas a partir dela
    possuiu_olho = True
    possuiu_boca = True

    def __init__(self, nome, idade):
        # atributo de instancia
        self.nome = nome
        self.idade = idade

    #  método de instancia
    def retorna_nome(self):
        return self.nome

    # método de instancia
    def logar_sistema(self):
        print(f'{self.retorna_nome()} esta logando no sistema')

    # método de classe é acessado apenas pela classe, o cls aponta para a classe
    @classmethod
    def altera_possui_boca(cls):
        cls.possuiu_boca = False
        return None

    # - método estático é apenas um utilitario,
    # - não tem acesso a atributos de classe ou de instancia
    # - só pode ser acessado pela classe e.g Pessoas.is_adulto(21)
    @staticmethod
    def is_adulto(idade):
        if idade > 10:
            return True
        return False
