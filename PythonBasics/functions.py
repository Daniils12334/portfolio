# function - a block of code that only runs when it is called

def happy_birthday(name, age):
    print(f"Happy Birthday {name}!")
    print(f"Youre now {age} years old!")

happy_birthday("Bro", 20)


def create_name(first_name,last_name):
    firs = first_name.capitalize()
    las = last_name.capitalize()
    return firs + " " + las

print(create_name("john", "doe"))