class Point:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f"{self.a}{self.b}"

    def __eq__(self, other):
        return self.num1 == other.num1 and self.num2 == other.num2

    def __gt__(self, other):
        return self.num1 > other.num1 and self.num2 > other.num2


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)

# A function that takes in a string
# If contains lowercase letters return the indexes of the lowercase letters