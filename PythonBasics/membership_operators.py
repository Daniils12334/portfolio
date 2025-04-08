#membership operators are used to test if a sequence is presented in an object

word = "APPLE"
letter = input("Guess a letter in the word: ")
if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

students = {"John", "Jane", "Tom", "Jerry"}
student = input("Enter a student name: ")
if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")

grades = {"John": 90, "Jane": 80, "Tom": 70, "Jerry": 60}
student = input("Enter a student name: ")
if student in grades:
    print(f"{student} has a grade of {grades[student]}")
else:

    print(f"{student} was not found")
#membership operators are used to test if a sequence is presented in an object
#in and not in are the membership operators in python

email = "tmsthe4@gmail.com"
if "@" not in email and "." not in email:
    print("invalid Email")
else:
    print("valid Email")