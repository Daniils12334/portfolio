fruits = [ "apple", "banana", "cocount" ]
vegetables = [ "carrot", "potato", "onion" ]
meats = [ "beef", "chicken", "fish" ]

groceries = [fruits, vegetables, meats]
for grocery in groceries:
    for food in grocery:
        print(food)
print(groceries[1][2]) # onion
print(groceries[0][1]) # banana
