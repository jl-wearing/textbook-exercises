#Function to continuously greet people.

def get_formatted_name(first_name, l_name):
    """Return a full name, neatly formatted."""
    return f"{first_name.title()} {l_name.title()}"

while True:
    print("Please tell me your name: ")
    print("enter 'q' to quit at any time.")

    #Input.
    f_name = input('First name: ')
    if f_name == 'q':
        break

    l_name = input('Last Name: ')
    if l_name == 'q':
        break

    #Process and Output.
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}.\n")
