from python.inheritance.animal import Animal


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2
    def walk(self):
        print("I am walking")


m = Mammal()
print(m.age)
print(isinstance(str, Mammal))

# function that finds the most repeated name in a list and return the item
