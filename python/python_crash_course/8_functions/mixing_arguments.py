def make_pizza(size, *toppings, flavor='lemon and herb'):
    """Display information the pizza we are about to make."""
    print(f"Making a {size}-size pizza of flavor {flavor} with the following toppings: ")

    for topping in toppings:
        print(f"- {topping}")

#Testing the make_pizza() function.
make_pizza('large', 'salami', 'olives', 'mushrooms', 'extra cheese', flavor='medium')
