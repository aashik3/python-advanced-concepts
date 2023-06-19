class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

# Create instances of the classes
rectangle = Rectangle("Rectangle", 4, 5)
circle = Circle("Circle", 3)

# Call the area() method on different objects
print(rectangle.area())  # Output: 20
print(circle.area())     # Output: 28.26
