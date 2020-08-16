# An example of class inheritance

class Animal(object):
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        print(f"{self.name} is eating {food}")

class Dog(Animal):
    def fetch(self, thing):
        print(f"{self.name} goes after the {thing}")

r = Dog("Rover")
r.fetch("paper")
r.eat("dog food")
