class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old.")

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary}")

    def greet(self):
        super().greet()
        print("I am an employee.")

class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, team):
        super().__init__(name, age, emp_id, salary)
        self.team = team

    def display_info(self):
        super().display_info()
        print(f"Team: {self.team}")

    def greet(self):
        super().greet()
        print("I am a manager.")

# Create instances of the classes
person = Person("John", 30)
person.greet()  # Output: Hello, my name is John. I am 30 years old.

employee = Employee("Alice", 25, "E123", 5000)
employee.greet()  # Output: Hello, my name is Alice. I am 25 years old. \n I am an employee.
employee.display_info()  # Output: Employee ID: E123 \n Salary: $5000

manager = Manager("Bob", 35, "M456", 8000, "Sales")
manager.greet()  # Output: Hello, my name is Bob. I am 35 years old. \n I am an employee. \n I am a manager.
manager.display_info()  # Output: Employee ID: M456 \n Salary: $8000 \n Team: Sales
