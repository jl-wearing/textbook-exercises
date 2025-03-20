def build_sandwich(*ingredients):
    """Create a sandwich out of the specified ingredients."""
    return ingredients

def describe_sandwich(sandwich):
    """Describe the ingredients in a sandwich."""
    print("This sandwich has the following ingredients: ")
    for ingredient in sandwich:
        print(f"- {ingredient.title()}")
    print()

#Testing the set of methods.
delicious_sandwich = build_sandwich('lettuce', 'fried egg', 'bacon', 'hashbrown', 'beef patty')
describe_sandwich(delicious_sandwich)