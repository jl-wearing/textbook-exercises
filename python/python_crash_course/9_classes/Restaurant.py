class Restaurant:
    """Attempt to model a simple restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """A restaurant is described by its name and cuisine type."""
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant attributes."""
        print(f"Restaurant Name: {self.name.title()}")
        print(f"Cuisine Type:    {self.cuisine_type}\n")

    def open_restaurant(self):
        """Indicate to customers that the restaurant is open for business."""
        print(f"{self.name.title()} is open for business.\n")

    def set_number_served(self, number):
        """Set the number of customers served."""
        if number <= self.number_served:
            print(f"Cannot reduce number of customers served.")
        else:
            self.number_served+= number

    def increment_number_served(self, addition):
        """Increments the number of customers served by a specified value."""
        if addition <= 0:
            print(f"Cannot reduce number of customers served.")
        else:
            self.number_served+= addition

#Testing the implementation of the class and its methods.
#Getters
kfc = Restaurant('kfc', 'fast food')
print(f"The restaurant's name is {kfc.name}.")
print(f"Cuisine Type: {kfc.cuisine_type}.\n")

#Testing the describe_restaurant() method.
kfc.describe_restaurant()

#Testing the open_restaurant() method.
kfc.open_restaurant()

#ex9_1 to add number_served attribute, change it, and display the change.
print(f"Number of customers served: {kfc.number_served}")
kfc.number_served = 100
print(f"Update on customers served: {kfc.number_served}\n")

#testing the set_number_served() method.
kfc.set_number_served(50)
kfc.set_number_served(200)
print(f"Update on customers served: {kfc.number_served}\n")

#testing the increment_number_served() method.
kfc.increment_number_served(-4)
kfc.increment_number_served(1000)
print(f"Update on customers served: {kfc.number_served}\n")