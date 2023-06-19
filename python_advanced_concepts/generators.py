# Generator function that yields the squares of numbers up to a given limit
def square_generator(limit):
    for i in range(1, limit + 1):
        yield i ** 2

# Create a generator object using the square_generator() function
squares = square_generator(10)

# Iterate over the generated squares using a for loop
for square in squares:
    print(square)

# Generator expression to generate the cubes of numbers up to a given limit
cubes = (i ** 3 for i in range(1, 10))

# Iterate over the generated cubes using a for loop
for cube in cubes:
    print(cube)

# Generator function to yield even numbers up to a given limit
def even_numbers(limit):
    for i in range(2, limit + 1, 2):
        yield i

# Create a generator object using the even_numbers() function
evens = even_numbers(10)

# Iterate over the generated even numbers using a for loop
for even in evens:
    print(even)

# Generator function to yield Fibonacci numbers up to a given limit
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Create a generator object using the fibonacci() function
fib_nums = fibonacci(100)

# Iterate over the generated Fibonacci numbers using a for loop
for fib_num in fib_nums:
    print(fib_num)

# Generator function that yields a countdown from a given number
def countdown(num):
    while num >= 0:
        yield num
        num -= 1

# Create a generator object using the countdown() function
countdown_gen = countdown(5)

# Iterate over the generated countdown using a for loop
for count in countdown_gen:
    print(count)

# Generator function that yields prime numbers up to a given limit
def primes(limit):
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

# Create a generator object using the primes() function
prime_nums = primes(20)

# Iterate over the generated prime numbers using a for loop
for prime in prime_nums:
    print(prime)

# Generator function that yields random numbers between a given range
import random

def random_numbers(start, end, count):
    for _ in range(count):
        yield random.randint(start, end)

# Create a generator object using the random_numbers() function
random_gen = random_numbers(1, 100, 5)

# Iterate over the generated random numbers using a for loop
for random_num in random_gen:
    print(random_num)
