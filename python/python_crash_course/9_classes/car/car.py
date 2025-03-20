"""A class that can be used to represent a car."""

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