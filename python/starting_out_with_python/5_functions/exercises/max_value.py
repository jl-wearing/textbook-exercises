def max_value(a, b):
    """Determine which number is larger."""
    if a > b:
        return a
    return b

def get_input():
    """Get numbers as input from the user."""
    first = int(input('Enter first number: '))
    second = int(input('Enter second number: '))

    return first, second

def main():
    """Mainline logic for the max number program."""
    #Get input from the user.
    first, second = get_input()

    #Determine the largest number.
    largest_number = max_value(first, second)

    #Output
    print(f"\nThe largest number is {largest_number}.")

#Call the main function.
if __name__ == '__main__':
    main()