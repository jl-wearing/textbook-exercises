"""Module to convert between mL and cups."""

MILLILITRES = 236.588

def starting_screen():
    """Display information about what the program does."""
    print("This program converts between millilitres and cups.")
    print("1 cup = 236.588mL")

def convert_to_ml(cups):
    """Convert cups to mL."""
    return cups * MILLILITRES

def convert_to_cups(millilitres):
    """Convert mL to cups."""
    cups = f"{millilitres/MILLILITRES:.1f}"
    return float(cups)

def main():
    """Mainline logic for the conversion program."""
    starting_screen()

    prompt = "Would you like to convert to:"
    prompt+= "\n1) cups"
    prompt+= "\n2) millilitres"
    prompt+= "\nq) to quit\n"

    while True:
        choice = input(prompt)

        if choice == 'q':
            break
        if choice == '1':
            #Input
            millilitres = float(input('\nHow many millilitres would you like to convert: '))

            #Process
            cups = convert_to_cups(millilitres)

            #Output
            print(f"{millilitres:.3f}mL gets you {cups:.1f} cups.\n")
        elif choice == '2':
            #Input
            cups = float(input('\nHow many cups would you like to convert: '))

            #Process
            millilitres = convert_to_ml(cups)

            #Output
            print(f"{cups:.1f} cups gets you {millilitres:.3f}mL.\n")
        else:
            print("Invalid choice!")


#Call the main function.
main()