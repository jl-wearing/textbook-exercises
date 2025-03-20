# Program to analyse numbers entered by the user.

# Constants used by the program.
NUMBER_OF_ELEMENTS_NEEDED = 20

def main():
    """Mainline logic for analysing numbers entered by the user."""
    numbers = []
    i = 0
    while i < 20:
        try:
            # Get a number from the user.
            number = int(input(f'Enter number {i+1}:'))
            numbers.append(number)
        except TypeError:
            print("Please enter a valid number!")
        except ValueError:
            print("Please enter a valid number!")
        except Exception as err:
            print(f"An error as occurred: {err}")
        else:
            i+=1

    # Determine the largest & smallest numbers entered.
    largest_number = max(numbers)
    smallest_number = min(numbers)

    # Determine the total and average of the numbers entered.
    total = sum(numbers)
    average = total / len(numbers)

    # Output
    print(f"\nLowest number: {smallest_number}")
    print(f"Largest number: {largest_number}")
    print(f"Total: {total}")
    print(f"Average: {average}\n")

# Call the main function.
if __name__ == '__main__':
    main()