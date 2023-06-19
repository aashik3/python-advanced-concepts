import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description='Example Argument Parser')

# Add positional argument
parser.add_argument('name', help='Name of the person')

# Add optional argument
parser.add_argument('--age', type=int, help='Age of the person')

# Add flag argument
parser.add_argument('--is_student', action='store_true', help='Whether the person is a student')

# Parse the command-line arguments
args = parser.parse_args()

# Access the parsed arguments
print('Name:', args.name)
print('Age:', args.age)
print('Is Student:', args.is_student)
