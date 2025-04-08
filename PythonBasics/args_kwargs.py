# *args = allows us to pass a variable number of arguments to a function.
# **kwargs = allows us to pass a variable number of keyword arguments to a function.

def add(*smthing):
    for arg in smthing:
        print(arg)
    return sum(smthing)

print(add(1,2,3,4,5,6,7,8,9,10))

def display_name(*names):
    for name in names:
        print(name, end = " ")

display_name("John", "Doe", "Jane", "Smith", "Tom", "Jerry", "\n")

def display_info(**info):
    print(type(info))
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name = "John", age = 20, country = "USA", city = "NYC")
