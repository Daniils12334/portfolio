name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hi {name}")

age = int(input("Enter your age: "))
while age < 0 or age > 120:
    print("Error: Age is incorrect")
    age = int(input("Enter your age: "))

#while not smthing == True: