#Program to write random numbers to a file.

import random

#Constants used by the program.
FILE_PATH = 'files/numbers.txt'

def main():
    """Mainline logic for writing random numbers to a file."""
    try:
        #Get the quantity of numbers to write to the file.
        size_of_numbers = int(input('Enter the size of data to generate: '))

        #Open the file for writing.
        output = open(FILE_PATH, 'w')

        #generate random numbers and add them to the file.
        for num in range(1, size_of_numbers+1):
            data = str(random.randint(1, 500))
            output.write(data + '\n')

        #Close the file.
        output.close()
    except ValueError:
        print("Please enter valid numbers as input!")
    except Exception as err:
        print(f"An error has occurred: {err}")

#Call the main function.
if __name__ == '__main__':
    main()