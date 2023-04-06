class Cart:
    def __init__(self, qtd, value):
        self.qtd = qtd
        self.value = value

    # def total(self):
    #     return
    def __add__(self, add):
        return self.qtd

    # def __del__(self):
    #     print("object is being deconstructed!")


c1 = Cart(10, 9)
c2 = Cart(10, 9)


c3 = c1 + c2