class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration()

# Create an instance of the MyIterator class
my_iterator = MyIterator(5)

# Iterate over the elements using a for loop
for num in my_iterator:
    print(num)

# Output: 0, 1, 2, 3, 4
