#Program to determine the insurance required for a building
#Constants required for the program.
INSURANCE_RATE = 0.8

def get_replacement_cost():
    """Get the cost to replace a building or home."""
    try:
        replacement_cost = float(input('Enter the cost to replace the building you wish to insure: '))
    except TypeError:
        print("Enter valid data, please.")
    except ValueError:
        print("Enter valid data, please.")
    else:
        return replacement_cost

def calculate_insurance(replacement_cost):
    """Calculate the insurance required to insure a building."""
    try:
        insurance_required = replacement_cost * INSURANCE_RATE
    except TypeError:
        pass
    else:
        return insurance_required

def main():
    """Mainline logic for the insurance program."""
    rep_cost = get_replacement_cost()
    insurance_required = calculate_insurance(rep_cost)

    #Output
    print(f"\nFunds required to insure your building: ${insurance_required:.2f}.\n")

if __name__ == '__main__':
    main()