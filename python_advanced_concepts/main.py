from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class implementing Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Concrete class implementing Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Create instances of the concrete classes
rectangle = Rectangle(5, 4)
circle = Circle(3)

# Call methods on the instances
print(rectangle.area())    # Output: 20
print(rectangle.perimeter())    # Output: 18
print(circle.area())    # Output: 28.26
print(circle.perimeter())    # Output: 18.84
