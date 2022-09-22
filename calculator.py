""" Method Chaining """


class Calculator:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Number = {self.number}"

    @property
    def half(self):
        self.number /= 2
        return self

    @property
    def double(self):
        self.number *= 2
        return self


c = Calculator(10)
print(c)
print(c.double.double)
print(c.half)
