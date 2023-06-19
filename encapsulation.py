class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
        self._odometer = 0

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def get_odometer(self):
        return self._odometer

    def set_odometer(self, value):
        if value >= self._odometer:
            self._odometer = value
        else:
            print("Invalid odometer value!")

    def drive(self, distance):
        print(f"Driving {distance} miles.")
        self._odometer += distance

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Accessing attributes using getter methods
print(my_car.get_make())   # Output: Toyota
print(my_car.get_model())  # Output: Camry
print(my_car.get_year())   # Output: 2020

# Accessing and modifying the odometer using getter and setter methods
print(my_car.get_odometer())  # Output: 0
my_car.set_odometer(100)
print(my_car.get_odometer())  # Output: 100

# Trying to set an invalid odometer value
my_car.set_odometer(50)  # Output: Invalid odometer value!

# Driving the car and updating the odometer
my_car.drive(150)
print(my_car.get_odometer())  # Output: 250
