#static methods = A method that belong to a class rather than any object from that class (instance)
#                 Usually used for general utility functions

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
#Instance metthods = Best for operations on instance of the class (objects)
    def get_info(self):
        return f"{self.name} = {self.position}"
#static methods = Best for utility functions that do not need acess to class data
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Laris", "Cashier")
employee3 = Employee("Alex", "Cook")



print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Dolbajobs"))
print(employee1.get_info())