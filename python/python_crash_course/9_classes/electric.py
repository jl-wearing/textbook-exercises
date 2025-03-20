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


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year, battery_size):
        """
        Initialize attributes of the parent class.
        Then, initialize attributes that are specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_battery(self):
        """Display information about the battery size."""
        print(f"This car has a {self.battery_size}kWh battery.")

    def get_descriptive_name(self):
        details = f"{self.make} {self.model} {self.year} {self.battery_size}kWh"
        return details.title()


tesla = ElectricCar('tesla', 'model s', 2025, 40)
print(tesla.get_descriptive_name())
tesla.describe_battery()