""" A static method does not receive an implicit first argument. S static method is also a method that is bound
to the class and not the object of the class. This method can't access or modify the class state. It is present
in a class because it makes sense for the method to be present in class"""

from random import randint


class Person:
    current_year = 2022

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birthday(self):
        print(self.current_year - self.age)

    @classmethod
    def birthday_year(cls, name, birthday):
        age = cls.current_year - birthday
        return cls(name, age)

    @staticmethod
    def generate_id():
        rand = randint(10000, 19999)
        return rand


p1 = Person.birthday_year('Helton', 29)
print(p1.name, p1.age)
# p1.get_birthday()
# print(p1.age)
# p1.get_birthday()
print(Person.generate_id())
