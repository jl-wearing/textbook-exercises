import random

# Constants used by the program.
MIN = 0
MAX = 9
NUMBER_OF_ELEMENTS = 7

def generate_numbers():
    """Generate and return random numbers."""
    return random.randint(MIN, MAX)

def fill_list():
    """Fill a list with random numbers."""
    random_numbers = []
    for i in range(NUMBER_OF_ELEMENTS):
        random_numbers.append(generate_numbers())

    return random_numbers

def print_lottery_numbers(data):
    """Display the lottery numbers generated."""
    print("These are your lottery numbers: ")
    for num in data:
        print(num, end=' ')
    print()

def main():
    """Mainline logic for displaying lottery numbers."""
    # Create a list with random lottery numbers.
    lottery_numbers = fill_list()

    # Display the lottery numbers.
    print_lottery_numbers(lottery_numbers)

# Call the main function.
if __name__ == '__main__':
    main()