from math import pi


class Circle:

    def __init__(self, r):
        self.r = r
        self.pi = pi

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, radius):

        if radius < 0:
            raise ValueError("Radius cannot be set to a negative value")
        self.__r = radius

    def area_of_circle(self):
        return f"the area of a circle with {self.r} is {self.pi * (self.r ** 2)}"

    def perimeter_of_circle(self):
        return f"the perimeter of circle with {self.r} is {2 * self.pi * self.r}"

    def __str__(self):
        return f"{self.r}"


circle = Circle(-33)
print(circle)
