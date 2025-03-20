# Program to filter a list out to only numbers > 0.

# Constants used by the program
NUMBERS = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

def main():
    """Mainline logic for filtering out negative numbers."""
    valid_numbers = []
    for number in NUMBERS:
        if number > 0:
            valid_numbers.append(number)

    # Calculate the total.
    total = calculate_total(valid_numbers)

    # Calculate the average.
    average = calculate_average(valid_numbers)

    # Output
    print(f"Total: {total:.2f}\n")
    print(f"Average: {average:.2f}\n")

def calculate_total(data):
    """Calculate the sum of all numbers in a list."""
    return sum(data)

def calculate_average(data):
    """Calculate the average of all numbers in a list."""
    return sum(data) / len(data)

# Call the main function.
if __name__ == '__main__':
    main()