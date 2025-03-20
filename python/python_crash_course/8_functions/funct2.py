#Define a function to greet a user.

def greet_user(name):
    """Display a greeting to a user."""
    print(f"Hello {name.title()}")

greet_user(input('Enter your name: '))