from car import Car


car1 = Car("Toyota_supra", 2008, "blue", False)
print(car1.model)
print(car1.year)
car2 = Car("Corvette", 2025, "red", True)
print(car2.for_sale)        

car1.stop()
car1.describe()