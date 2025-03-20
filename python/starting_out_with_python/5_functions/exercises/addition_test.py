import random

def generate_questions(number_of_questions):
    """Generate simple questions and display them to the user."""
    for i in range(number_of_questions):
        print(f"{random.randint(1, 10)} + {random.randint(1, 10)} = _____")
    print()

def get_number_of_questions():
    """Get the number of questions from the user."""
    while True:
        try:
            number_of_questions = int(input("Enter the number of "
                                            "questions to answer: "))
            break
        except ValueError:
            print("Enter a valid number please!")
    return number_of_questions

def main():
    """Mainline logic for the question program."""
    #Get the number of questions to solve from the user.
    number_of_questions = get_number_of_questions()

    #Display the questions.
    generate_questions(number_of_questions)

#Call the main function.
if __name__ == '__main__':
    main()