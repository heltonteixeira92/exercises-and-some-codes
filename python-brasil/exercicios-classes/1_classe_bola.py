class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, cor):
        self.cor = cor

    def mostra_cor(self):
        return self.cor


bola = Bola('verde', 'redonda', 'plastico')
print(bola.mostra_cor())
