class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type.")

# Create two Vector objects
v1 = Vector(2, 3)
v2 = Vector(1, 4)

# Use the "+" operator to add two Vector objects
v3 = v1 + v2

# Display the result
print(v3)  # Output: Vector(3, 7)
