'''Type hinting in Python allows you to annotate your code with information about
 the expected types of variables, function arguments, and return values'''
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    return a + b

def calculate_average(numbers: List[float]) -> float:
    total = sum(numbers)
    return total / len(numbers)

# Function with type hint for return value as None
def log_message(message: str) -> None:
    print(f"Log: {message}")

# Function with type hint for a dictionary
def process_data(data: Dict[str, Union[int, str]]) -> None:
    for key, value in data.items():
        print(f"{key}: {value}")

# Function with type hint for an optional argument
def print_age(name: str, age: Optional[int] = None) -> None:
    if age is not None:
        print(f"{name} is {age} years old.")
    else:
        print(f"Age not provided for {name}.")

# Function with type hint for a generator
def generate_numbers(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i

# Variable with type hint
count: int = 5

# List with type hint
numbers: List[float] = [1.5, 2.3, 4.7]

# Dictionary with type hint
person: Dict[str, Union[str, int]] = {'name': 'John', 'age': 30}

# Usage of the functions and variables
print(greet("Alice"))
print(add_numbers(10, 20))
print(calculate_average(numbers))
log_message("An error occurred.")
process_data(person)
print_age("Bob", 25)
for num in generate_numbers(5):
    print(num)
print(count)
