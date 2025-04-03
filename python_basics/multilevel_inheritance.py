#multilevel inheritance = C(B) <- B(A) <- A
#multiple inheritance = inherit from more then one parent class C(A, B)

class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")
class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

rabbit = Rabbit("Bob")
hawk = Hawk("James")
fish = Fish("Linda")

hawk.hunt()
fish.flee()
fish.hunt()

rabbit.eat()
