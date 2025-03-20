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

#testing the implementation of the class and its methods.
#getters
audi = Car('audi', 'rs e-tron', 2025)
print(f"{audi.make} {audi.model} {audi.year} {audi.mileage}")

#testing the get_descriptive_name() method.
about = audi.get_descriptive_name()
print(about, '\n')

#testing the read_odometer() method.
audi.read_odometer()
audi.mileage = 1_000
audi.read_odometer()
audi.update_odometer(500)
audi.read_odometer()

#testing the increment_odometer() method.
audi.increment_odometer(400)
audi.read_odometer()