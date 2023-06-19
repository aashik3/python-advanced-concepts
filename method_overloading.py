'''In Python, method overloading is not directly supported as it is in some other programming
 languages like Java or C++. However, you can achieve similar functionality by using default
 arguments or variable-length arguments'''
class Calculator:
    def add(self, num1, num2=None):
        if num2 is None:
            return num1
        else:
            return num1 + num2

# Create an instance of the Calculator class
calc = Calculator()

# Call the add() method with different arguments
result1 = calc.add(5)
result2 = calc.add(3, 7)

# Display the results
print(result1)  # Output: 5
print(result2)  # Output: 10
