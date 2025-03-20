#There are numerous ways to pass arguments.

#The first way is posititonal arguments where you specify the arguments in the
#order in which they were defined.
def describe_pet(animal_type, animal_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name.title()}.\n")

def drive(name, age):
    """Determine if a person is old enough to drive."""
    if age >= 18:
        print(f"{name.title()}, you are old enough to drive!\n")
    else:
        print(f"Wait {18 - age} years before you can get a license!\n")

#Testing the arguments that use posititional arguments.
describe_pet('dog', 'kiwi')
describe_pet('dog', 'ziggy')
drive('nigel', 14)
drive('justin', 23)

#A keyword argument is a name-value pair that you pass to a function.
#You directly associate the argument with the parameter.
#Thus, you can describe the arguments in any order you wish.
describe_pet(animal_name='Lila', animal_type='dog')
drive(name='shaun', age=30)

#Default values
#When writing a function, you can define a default value for each parameter.
#If an argument is provided for a parameter, python uses the argument.
#If no argument is supplied, python uses the default value.
#NOTE: Default arguments must be specified last in the function definition.
#NOTE: This is because the default argument makes it unnecessary to specify that argument.
def default_pet(animal_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name.title()}.\n")

#Testing the function with default values.
default_pet('aron')
default_pet(animal_name='nala')
default_pet('kfc', 'bird')

#When you use default valies, any parameter with a default value needs to be
#listed after all parameters that don't have default values. This allows Python
#to continue interpreting positional arguments correctly.

#Positional, keyword and default arguments tend to produce equivalent function calls.
#Use the one you find easiest to understand and be consistent with it.