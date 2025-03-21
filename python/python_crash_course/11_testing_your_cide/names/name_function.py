def get_formatted_name(first, last, middle=''):
    """Return a neatly formatted name."""
    if  middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()