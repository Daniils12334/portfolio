name = input("Enter your name: ")
phone_number = input("Enter your phone number: ")

result = len(name) # len() is a built-in function that returns the length of a string
result = name.find("a") # find() is a built-in function that returns the index of the first occurence of the given character in the string
result = name.rfind("a") # rfind() is a built-in function that returns the index of the last (returned) occurence of the given character in the string
name = name.capitalize() # capitalize() is a built-in function that capitalizes the first letter of the string
name = name.upper() # upper() is a built-in function that converts all the letters in the string to uppercase
name = name.lower() # lower() is a built-in function that converts all the letters in the string to lowercase
name = name.title() # title() is a built-in function that capitalizes the first letter of each word in the string
name = name.strip() # strip() is a built-in function that removes the leading and trailing whitespaces in the string
name = name.replace(" ", "-") # replace() is a built-in function that replaces the first argument with the second argument in the string
result = name.isdigit() # isdigit() is a built-in function that returns True if all the characters in the string are digits
result = name.isalpha() # isalpha() is a built-in function that returns True if all the characters in the string are alphabets
result = phone_number.count("-") # count() is a built-in function that returns the number of occurences of the given character in the string``



if len(name) > 12:
    print("Your name is too long")
elif not name.find(" ") == -1:
    print("Your name should not contain spaces")
elif not name.isalpha():
    print("Your name cant contain numbers")
else:
    print(f"Hi {name}, your phone number is {phone_number}")