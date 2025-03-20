"""A set of classes that can be used to describe an electric car."""
from car import Car

class Battery:
    """A simple attempt to model a battery of an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}kWh battery.")

    def get_range(self):
        """Get the range this battery provides."""
        MULTIPLIER = 2.5
        return self.battery_size * MULTIPLIER

    def battery_upgrade(self, new_size):
        """Change the capacity of the battery."""
        self.battery_size = new_size

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric cars."""

    def __init__(self, make, model, year, battery_size=40):
        """
        Initialize the attributes of the superclass.
        Then initialize the attributes specific to electric cars.
        """
        super().__init__(make, model, year)
        self.battery = Battery(battery_size)

    def get_descriptive_name(self):
        """Describe the details of the car."""
        details = f"{self.make} {self.model} {self.year} {self.battery.battery_size}kWh"
        return details.title()