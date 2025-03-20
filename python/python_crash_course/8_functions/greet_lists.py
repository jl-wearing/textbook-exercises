def greet_users(usernames):
    """Display a greeting to each user in the list."""
    for name in usernames:
        print(f"Hello, {name}")

    print()

def sanitize_list(data):
    """Convert all usernames to lowercase."""
    sanitized = []
    while data:
        #retrieve a user.
        name = data.pop()

        #convert to lowercase and add to sanitized list.
        sanitized.append(name.lower())

    #get the original ordering.
    sanitized.reverse()

    return sanitized

#Testing the greet_users() function.
users = ['pessi', 'penaldo', 'cole penmer', 'luis bite-ez']
greet_users(users)
print()

#Testing the sanitize_list() function.
animals = ['COWS', 'DOGS', 'FISH', 'PIGS']
animals = sanitize_list(animals)
print(animals)
print()
