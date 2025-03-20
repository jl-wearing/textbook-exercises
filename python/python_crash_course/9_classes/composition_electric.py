class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def get_descriptive_name(self):
        """Summarize the car in a neatly formatted way."""
        details = f"{self.make} {self.model} {self.year}"
        return details.title()

    def read_odometer(self):
        """Get the mileage of this car."""
        print(f"This car has {self.mileage} miles on it.")

    def update_odometer(self, mileage):
        """Set the mileage of this car to the specified mileage."""
        if mileage > self.mileage:
            self.mileage = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        """Increment the odometer by the specified miles."""
        if miles <= 0:
            print("You cannot set negative miles.")
        else:
            self.mileage += miles


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

    def __init__(self, make, model, year, battery_size):
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


leaf = ElectricCar('nissan', 'leaf', '2025', 100)
print(leaf.get_descriptive_name())
leaf.battery.describe_battery()
print(f"Range: {leaf.battery.get_range()}")
print()

leaf.battery.battery_upgrade(150)
print(leaf.get_descriptive_name())
print(f"Range: {leaf.battery.get_range()}")