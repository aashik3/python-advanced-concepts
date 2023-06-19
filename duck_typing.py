
class Duck:
    def quack(self):
        print("Quack!")

    def fly(self):
        print("Flap, flap!")

class Mallard:
    def quack(self):
        print("Quack!")

    def fly(self):
        print("Flap, flap!")

class Airplane:
    def fly(self):
        print("Zoom, zoom!")

# Define a function that takes any object and performs specific actions
def perform_actions(obj):
    obj.quack()
    obj.fly()

# Create instances of the Duck, Mallard, and Airplane classes
duck = Duck()
mallard = Mallard()
airplane = Airplane()

# Call the perform_actions() function with different objects
perform_actions(duck)      # Output: Quack! \n Flap, flap!
perform_actions(mallard)   # Output: Quack! \n Flap, flap!
perform_actions(airplane)  # Output: Zoom, zoom!
