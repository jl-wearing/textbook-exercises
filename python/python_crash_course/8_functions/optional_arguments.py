def get_formatted_name(first_name, last_name, middle_name=''):
    """Display a neatly formatted name."""
    #Python evaluates non-empty strings to true.
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

#Testing the get_formatted_name() function.
name = get_formatted_name('justin', 'wearing', 'leon')
print(name)
print(get_formatted_name('lionel', 'messi'))