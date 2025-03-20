#You can define a default argument for each parameter in the function definition.
#If an argument is provided in a function call, Python uses that value. Otherwise, it uses the default value.
#Default arguments are defined last in a function definition.

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")

#Testing the describe_pet() function.
#1. Positional Arguments.
describe_pet('nandos', 'chicken')

#2. Keyword Arguments.
describe_pet(animal_type='cow', pet_name='barbeque')
describe_pet(pet_name='nala')

#3. Default Arguments.
describe_pet('lila')