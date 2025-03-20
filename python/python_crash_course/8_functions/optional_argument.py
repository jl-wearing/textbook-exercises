#Sometimes it makes sense to make an argument optional, so that
#people using the function can provide additional information only
#if they wish to do so.
#Using empty strings makes arguments optional.

def get_formatted_name(first_name, last_name, middle_name=''):
    """Display a neatly formatted full name."""
    return f"{first_name.title()} {middle_name.title()} {last_name.title()}"

#Testing the function.
full_name = get_formatted_name('justin', 'wearing', 'leon')
print(full_name)

full_name = get_formatted_name('Lionel', 'Messi')
print(full_name)


#Python interprets non-empty strings as True.
#Alternative definition of the function.
def get_formatted_2(first_name, last_name, middle_name=''):
    """Display a neatly formatted full name."""
    if middle_name:
        return f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        return f"{first_name.title()} {last_name.title()}"

#Testing the function.
full_name = get_formatted_2('justin', 'wearing', 'leon')
print(full_name)

full_name = get_formatted_2('Lionel', 'Messi')
print(full_name)
