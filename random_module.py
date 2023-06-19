import random

# Generate a random floating-point number between 0 and 1
random_number = random.random()
print("Random number between 0 and 1:", random_number)

# Generate a random integer within a specified range
random_int = random.randint(1, 10)
print("Random integer between 1 and 10:", random_int)

# Select a random element from a list
my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)
print("Random element from the list:", random_element)

# Shuffle the elements in a list randomly
random.shuffle(my_list)
print("Shuffled list:", my_list)

# Generate a random sample from a list without replacement
sample = random.sample(my_list, 3)
print("Random sample:", sample)

# Seed the random number generator for reproducibility
random.seed(123)
random_num_1 = random.random()
random_num_2 = random.random()
print("Random number 1:", random_num_1)
print("Random number 2:", random_num_2)
