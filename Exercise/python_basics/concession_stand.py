menu = {"pizza" : 3.00,
        "hot dog" : 2.00,
        "soda" : 1.00,
        "chips" : 0.50,
        "water" : 1.25}
cart =[]
total = 0
print("----------- Menu -----------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}$")
print("----------------------------")

while True:
    food = input("Select an item from the menu or type 'done' to finish: ").lower()
    if food == "done":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("----------- Order -----------")

for food in cart:
    total += menu.get(food)
    print(food, end=", ")

print(f"Total is: {total:.2f}$")