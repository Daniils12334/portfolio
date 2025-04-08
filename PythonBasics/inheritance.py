#class Child(parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speek(self):
        print("Woof")

class Cat(Animal):
    def speek(self):
        print("Meow")   

class Mouse(Animal):
    def speek(self):
        print("Squeek")

dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Mickey")

print(dog.name)
print(cat.is_alive)
cat.sleep()
cat.eat()
cat.speek()
dog.speek()
mouse.speek()