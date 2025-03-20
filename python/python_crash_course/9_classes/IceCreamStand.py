class Restaurant:
    """Attempt to model a simple restaurant."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
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

class IceCreamStand(Restaurant):
    """An ice cream stand is a type of restaurant, with specific attributes."""

    def __init__(self, restaurant_name, *flavors):
        """
        Initialize the attributes of the superclass.
        Then, initialize the attributes of the IceCreamStand class.
        :param restaurant_name: the name of the restaurant
        :param flavors: the list of flavors offered by this ice cream stand.
        """
        super().__init__(restaurant_name)
        self.flavors = list(flavors)

    def display_flavors(self):
        """Display the flavors offered by this ice cream stand."""
        print("\nHere are the flavors we offer: ")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")
        print()

#Testing the subclass.
milky_lane = IceCreamStand('milky lane', 'bar one', 'oreo', 'vanilla', 'chocolate')
milky_lane.describe_restaurant()
milky_lane.display_flavors()