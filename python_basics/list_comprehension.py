# List comprehjensions are a way to create lists in python
# They are a way to create lists in a more concise way

# doubles = []
# for x in range (1,11):
    # doubles.append(x*2)
# print(doubles)

doubles =[x * 2 for x in range(1,11)]
triples = [y * 3 for y in range(1,11)]
squares = [z ** 2 for z in range(1,11)]
print(doubles)
print(triples)
print(squares)

fruits = ['apple', 'banana', 'cherry', 'date']
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

numbers = [1,-2,3,-4,5,-6,7,-8,9]
positive_numbers = [num for num in numbers if num >= 0]
negative_numbers = [num for num in numbers if num <= 0]
print(positive_numbers)
print(negative_numbers)

grades = [85, 75, 24, 65, 90, 95, 70]
sorted_grades = ['Good' if grade >= 60 else 'Bad' for grade in grades]
print(sorted_grades)