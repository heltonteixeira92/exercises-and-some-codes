from datetime import datetime


class Person:
    current_year = int(datetime.strftime(datetime.now(), '%Y'))  # class attribute

    def __init__(self, name, age, eating=False, speaking=False):
        self.name = name  # instance attribute
        self.age = age
        self.eating = eating
        self.speaking = speaking

    def speak(self, subject):
        if self.eating:
            print(f'cannot speak, {self.name} is eating right now.')
            return

        if self.speaking:
            print(f'Already is speaking')
            return

        print(f'{self.name} is speaking about {subject}')
        self.speaking = True

    def stop_spek(self):
        if not self.speaking:
            print(f"{self.name} isn't speaking")
            return

        print(f'Stopping speak...')
        self.speaking = False

    def eat(self, food):
        if self.eating:
            print('Already is eating.')
            return
        if self.speaking:
            print(f'Cannot eat, {self.name} is speaking right now.')
            return

        print(f'{self.name} is eating {food}')
        self.eating = True

    def stop_eat(self):
        if not self.eating:
            print(f"{self.name} isn't eating.")
            return

        print(f'{self.name} stopped eat.')
        self.eating = False

    def get_birthday(self):
        return self.current_year - self.age
