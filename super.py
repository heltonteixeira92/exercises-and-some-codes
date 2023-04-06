class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def latir(self):
        print('au au')


class SmallAnimal(Animal):
    def __init__(self, name, age, kind):
        self.kind = kind
        super().__init__(name, age)



