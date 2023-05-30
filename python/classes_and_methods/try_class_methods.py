class Point:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        print(f"drawing from point {self.a} to {self.c}")
    @classmethod
    def point_from_one(cls):
        return cls(1, 1, 1)

    def __str__(self):
        return f"({self.a}, {self.b}, {self.c})"


p1 = Point(2, 3, 4)
p2 = Point(3, 5, 6)
p1.draw()
p1 = Point.point_from_one()
print(p1)

