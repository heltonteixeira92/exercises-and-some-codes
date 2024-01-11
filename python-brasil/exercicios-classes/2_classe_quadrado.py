class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado(self, novo_tamanho_lado):
        self.tamanho_lado = novo_tamanho_lado

    def mostrar_valor_lado(self):
        return self.tamanho_lado

    def calcular_area(self):
        """Um quadrado tem 4 lados/angulos iguais, são chamados de poligono regulares
            área do quadrado = lado x lado
        """
        return self.tamanho_lado * self.tamanho_lado


quadrado = Quadrado(17)
print(quadrado.calcular_area())
