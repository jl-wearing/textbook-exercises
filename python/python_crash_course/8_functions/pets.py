#Positional arguments need to be supplied in the order they appear in the function definition.

def describe_pet(animal_type, name):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {name.title()}.\n")

#Testing the describe_pet() function.
describe_pet('dog', 'kiwi')
describe_pet('dog', 'ziggy')

#Keyword arguments free you from specifying arguments in any order.
describe_pet(animal_type='bird', name='nandos')
describe_pet(name='BBQ', animal_type='cow')