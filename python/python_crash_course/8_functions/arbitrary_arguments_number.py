def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("Making a pizza with the following toppings: ")

    for topping in toppings:
        print(f"\t{topping.title()}")
    print()

#Testing the make_pizza() function.
make_pizza('salami')
make_pizza('olives', 'pineapple', 'salami')