class Human:
    number_of_eyes = 2
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello {self.name}")

    def walking(self):
        print(f"{self.name} is walking")

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def color_of_eyes(cls):
        return cls("brown")
    @classmethod
    def number_of_nose(cls):
        return cls(1)


human1 = Human("Esther Peter")
human2 = Human("Peter Pan")

print(f"{human1} has {human1.number_of_eyes} number of {human2.color_of_eyes()} eyes and {Human.number_of_nose()} number of nose")
print(f"And {human2} has {Human.number_of_eyes} number {Human.color_of_eyes()} of eyes and {human1.number_of_nose()} number of nose")
