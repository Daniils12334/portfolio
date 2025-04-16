#Shopping cart programming exercise

cart = []
total = 0
def add_item(item, price):
    global total
    cart.append(item)
    total += price
    print(f"{item} added to cart. Total: ${total:.2f}")
while True:
    add_item(input("Enter item: "), float(input("Enter price: ")))
    if input("Do you want to add more items? (y/n): ") == "n":
        break
print("Items in cart: ", cart)
print(f"Total: {total:.2f}$")