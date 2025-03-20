#Program to return a person's name.

def get_formatted_name(first_name, last_name):
    """Return a person's name, neatly formatted."""
    full_name = f"{first_name} {last_name}"

    return full_name.title()

#Testing the get_formatted_name() function.
print(get_formatted_name('justin', 'wearing'))

musician = get_formatted_name('jimi', 'hendrix')
print(musician)