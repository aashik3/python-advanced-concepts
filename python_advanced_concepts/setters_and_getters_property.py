class Celsius:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be less than -273.15°C")
        self._temperature = value

    @property
    def fahrenheit(self):
        return (self._temperature * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        celsius_value = (value - 32) * 5/9
        self.temperature = celsius_value

    @property
    def kelvin(self):
        return self._temperature + 273.15

    @kelvin.setter
    def kelvin(self, value):
        celsius_value = value - 273.15
        self.temperature = celsius_value


# Create a Celsius object
celsius = Celsius(25)

# Access the temperature in Celsius
print("Temperature in Celsius:", celsius.temperature)

# Access the temperature in Fahrenheit
print("Temperature in Fahrenheit:", celsius.fahrenheit)

# Access the temperature in Kelvin
print("Temperature in Kelvin:", celsius.kelvin)

# Update the temperature in Celsius
celsius.temperature = 30
print("Updated Temperature in Celsius:", celsius.temperature)

# Update the temperature in Fahrenheit
celsius.fahrenheit = 86
print("Updated Temperature in Celsius:", celsius.temperature)

# Update the temperature in Kelvin
celsius.kelvin = 303.15
print("Updated Temperature in Celsius:", celsius.temperature)
