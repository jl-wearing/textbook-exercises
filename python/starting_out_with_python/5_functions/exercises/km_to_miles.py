#Program to convert kilometres to miles.
#Constants that are used by the program.
MILE = 0.6214

def convert_to_miles(kilometres):
    """Converts to miles."""
    try:
        miles = kilometres * MILE
    except TypeError:
        print("Please enter valid numerical data.")
    else:
        return miles

def main():
    while True:
        try:
            kilometres = float(input('Enter kilometres to convert to miles: '))
        except ValueError:
            pass
        else:
            miles = convert_to_miles(kilometres)
            print(f"{kilometres}km is {miles} miles.\n")
            break

if __name__ == '__main__':
    main()