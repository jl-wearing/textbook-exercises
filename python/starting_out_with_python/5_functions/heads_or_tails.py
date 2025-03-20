import random

def starting_screen():
    """Display to the user the purpose of the program."""
    print("This program will toss a coin.")
    print("Your job is to correctly guess the face of the toss.")

def make_guess():
    """Retrieve a coin toss guess from the console."""
    prompt = "Please guess, heads or tails?: "
    choice = ""
    while choice != 'heads' and choice != 'tails':       #input validation
        choice = input(prompt)

    return choice

def correct_guess(choice):
    """Determine if the user guessed correctly."""
    correct_choice = random.choice(['heads', 'tails'])

    return correct_choice == choice

def main():
    """The mainline logic for the heads or tails game."""
    starting_screen()

    while True:
        choice = make_guess()
        correct_answer = correct_guess(choice)

        if correct_answer:
            print("You win! You guessed correctly.")
        else:
            print("Sorry! Better luck next time.")

        play_again = input("Would you like to play again? (y/n): ")
        if play_again == 'n':
            break

#Call the main function.
main()