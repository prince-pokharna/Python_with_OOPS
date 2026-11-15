
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")


person1 = Person("Max", 25)
person2 = Person("Alex", 30)

person1.introduce()
person2.introduce()

person1.birthday()
