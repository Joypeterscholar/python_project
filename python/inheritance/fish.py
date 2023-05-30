from python.inheritance.animal import Animal
from python.inheritance.mammal import Mammal


class Fish(Mammal):
    def swim(self):
        print("I am swimming")


animal = Fish()
animal.eat()
print(f"I am {animal.age} year(s) old")
print(animal.walk)
