""" I should use classmethod when my method be related to with my class and not instance"""

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


p1 = Person.birthday_year('Helton', 29)
print(p1.name, p1.age)
# p1.get_birthday()
# print(p1.age)
# p1.get_birthday()