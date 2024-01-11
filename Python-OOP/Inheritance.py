class Animal:

    possui_olho = True
    def __init__(self, name, species):
        # atributos de instancia
        self.name = name
        self.species = species

    # metodo de instancia
    def make_sound(self):
        return "alohaaa"


class Dog(Animal):
    # def __init(self, name, breed):
    #     super().__init__(name, species="Dog")
    #     self.breed = breed

    def make_sound(self):
        print('a')
        super().make_sound()


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def make_sound(self):
        return "Meow!"


# Usage of the classes
dog = Dog("Cookie", "Shitzu")
print(dog.name)
print(dog.make_sound())
