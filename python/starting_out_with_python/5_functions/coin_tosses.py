import random

NUMBER_OF_TOSSES = 10

def toss():
    """Toss a coin."""
    return random.choice(['heads', 'tails'])

def main():
    """Mainline logic for the coin toss program."""
    for i in range(NUMBER_OF_TOSSES):
        print(toss())
    print()

#Call the main function.
main()