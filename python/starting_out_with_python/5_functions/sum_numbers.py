#Program to sum 2 numbers.

def get_input():
    """Get numbers from the user to determine the sum."""
    numbers = []

    for i in range(2):
        while True:
            try:
                number = int(input(f"Enter number {i +1}: "))
                numbers.append(number)
                break
            except ValueError:
                print("Invalid Input! Please enter a valid number.")

    return numbers

def total(numbers):
    """Determine the sum of 2 numbers."""
    return sum(numbers)

def main():
    """Mainline logic for the summing program."""
    numbers = get_input()
    total = sum(numbers)

    #Output
    print(f"\n{numbers[0]} + {numbers[1]} = {total}.\n")

#Call the main function.
main()