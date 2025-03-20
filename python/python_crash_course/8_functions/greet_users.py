#Function to greet users in a list.

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    if names:
        for name in names:
            print(f"Hello, {name.title()}")
    else:
        print("There are no users!")

#Testing the function.
players = ['messi', 'suarez', 'busquets']
users = []
greet_users(players)
greet_users(users)