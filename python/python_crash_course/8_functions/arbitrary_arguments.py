#Sometimes you won't know ahead of times how many arguments a function
#needs to accept.
#Python allows a function to collect an arbitrary number of arguments.

#Function to build a pizza.
def build_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

#Testing the function.
build_pizza('mushrooms')
build_pizza('pepperoni', 'mushrooms', 'chicken', 'pineapple')
#The output is a tuple called toppings.

#Alternatively, because we know that a tuple is created, we can loop
#through it instead.

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

#Testing the function.
make_pizza('olives')
make_pizza('pineapple', 'olives', 'mushrooms')