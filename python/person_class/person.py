class Person:
    def greet(self):
        print("Person greeting")


class Admin:
    def greet(self):
        print("Admin greeting")

class Employee(Person, Admin):
    pass



class Text(str):
    def duplicate(self):
        return self + self

t1 = Text()


