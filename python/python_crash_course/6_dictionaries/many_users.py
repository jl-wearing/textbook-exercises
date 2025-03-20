#Nesting a dictionary inside another dictionary.
many_users = {
    'ein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for name, info in many_users.items():
    print(f"Username: {name}")
    full_name = f"{info['first'].title()} {info['last'].title()}"
    location = f"{info['location'].title()}"

    #Display data.
    print(f"\tFirst name: {full_name}")
    print(f"\tLocation: {location}")
print()