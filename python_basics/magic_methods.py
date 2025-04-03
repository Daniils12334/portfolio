#Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                They are automatically called by many of Python's built in operations
#                They allow developers to define or customize the behaviour of objects
# 
# class Student:
    # def __init__(self, name, gpa):
        # self.name = name
        # self.gpa = gpa
# 
    # def __str__(self):
        # return f"name: {self.name} gpa: {self.gpa}"
    # 
    # def __eq__(self, value):
        # return self.name == value.name
    # 
    # def __gt__(self, value):
        # return self.gpa > value.gpa
    # 
    # 
# student1 = Student("Spongebob", 3.2)
# student2 = Student("Ivan", 2.2)
# student3 = Student("Alena", 3.2)
# 
# print(student1)
# print(student1 == student2)
# print(student1 > student2)
# 
class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, value): # value means other book/second
        return self.title == value.title and self.author == value.author
    
    def __lt__(self, other):
        return self.num_pages > other.num_pages
    
    def __gt__(self, value):
        return self.num_pages < value.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__ (self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        if key == "author":
            return self.author
        if key == "num_pages":
            return self.num_pages

book1 = Book("The Hobbit", "John Ronald Ruel Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K Rowling", 233)
book3 = Book("The Witcher The Last Wish", "Andrzej Sapkowski", 453)

print(book3) #__str__
print(book1 == book2) #__eq__
print(book1 > book2) #__lt__
print(book1 < book2) #__gt__
print(book1 + book3) #__add__

print("Witcher" in book3)

print(book1['author'])