import random

#Constants to represent the minimum and maximum number of faces on a die.
MIN = 1
MAX = 6

def roll_die():
    """Perform the action of rolling a die."""
    return random.randint(MIN, MAX)

def main():
    """Mainline logic for the die-roll program."""
    while True:
        print("\n2 die rolls will be performed.")
        print(f"First roll:  {roll_die()}")
        print(f"Second roll: {roll_die()}")

        re_roll = input("Would you like to roll again? (y/n): ")
        if re_roll == 'n':
            break

#Call the main function.
main()