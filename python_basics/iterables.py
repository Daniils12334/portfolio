# iterables = list, tuple, set, dictionary, string
numbers = [1,2,3,4,5,6,7,8,9,10]

for number in reversed(numbers):
    print(number, end = " ")

fruits = {"A": "apple","B": "banana","C": "cherry","D": "orange"}

for fruits in reversed(fruits.values()):
    print(fruits, end = " ")