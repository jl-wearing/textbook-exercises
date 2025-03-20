#program to add 2 numbers.
def add():
    """Simple attempt to add 2 numbers."""
    print("Enter 2 numbers and I will add them up.")

    #input
    try:
        first_number = int(input('\nEnter first number: '))
        second_number = int(input('Enter second number: '))
    except ValueError:
        print(f"Enter numbers, not characters!")
    else:
        total = first_number + second_number
        print(f"{first_number} + {second_number} = {total}.\n")

#Testing the add() method.
for i in range(5):
    add()