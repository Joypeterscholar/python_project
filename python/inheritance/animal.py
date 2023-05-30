from abc import ABC, abstractmethod

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("I am eating")

    @abstractmethod
    def run(self):
        pass

class Mammal(Animal):
    def __init__(self):
        self.weight = 2
        super().__init__()

    def run(self):
        print("Running...")

    def run(self):
        print("R")

