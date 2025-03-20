#Python can return more than one value in a single return call.

def formatted_name():
    """Get a person's first and last name, neatly formatted."""
    first = input('Enter first name: ')
    last = input('Enter last name: ')
    return first.title(), last.title()

#testing
first, last = formatted_name()
print(first, last)