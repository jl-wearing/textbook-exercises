from name_function import get_formatted_name

def get_name():
    """Get user details from the keyboard."""
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')

    return get_formatted_name(first, last)

def main():
    """MAIN FUNCTION"""
    active = True
    while active:
        full_name = get_name()

        for name in full_name.split():
            if name.lower() == 'q':
                active = False
                break
        else:
            print(f"Neatly formatted name: {full_name}.\n")


#testing
main()