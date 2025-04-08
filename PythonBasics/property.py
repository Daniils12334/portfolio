# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you getter, setter, and deletter method

class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width
    @property
    def width(self):
        return f"{self._width:.1f}cm"
    @property
    def height(self):
        return f"{self._height:.1f}cm"
        

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater then 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width deleted")
    @height.deleter
    def height(self):
        del self._height
        print("Height deleted")


rectangle = Rectangle(5, 10)
rectangle.width = 20
rectangle.height = 30

del rectangle.width
del rectangle.height

# print(rectangle.width)
# print(rectangle.height)
# print(rectangle._height)
# print(rectangle._width)



        