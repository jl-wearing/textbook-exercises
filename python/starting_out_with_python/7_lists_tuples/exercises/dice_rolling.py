# Program to return a list of random numbers based on rolling a die.
import random

# Constants used by the program.
MIN = 1
MAX = 6

def roll(number_of_throws):
    """
    Roll a die a specified number of times and return a sorted
    list containing the die rolls.
    """
    rolls = []
    for die_roll in range(number_of_throws):
        rolls.append(random.randint(MIN, MAX))
    rolls.sort()

    return rolls

def get_input():
    """Get the number of times to roll the die from the user."""
    number_of_rolls = int(input('\nEnter the number of times to roll a die:' ))
    return number_of_rolls

def output_rolls(rolls):
    """Display the results of the die rolls."""
    for roll in rolls:
        print(roll, end=' ')
    print()

def main():
    """Mainline logic for rolling a die a specified number of times."""
    while True:
        # Get the number of rolls to perform.
        while True:
            try:
                number_of_rolls = get_input()
                break
            except ValueError:
                print("Enter a valid number.")
            except TypeError:
                print("Enter a valid number.")
            except Exception as err:
                print(f"An error has occurred: {err}")

        # Perform the die rolls.
        rolls = roll(number_of_rolls)

        # Output
        output_rolls(rolls)

        # Roll again.
        roll_again = input("Press enter to roll again or 'q' to quit: ")
        if roll_again == 'q':
            break

# Call the main function.
if __name__ == '__main__':
    main()