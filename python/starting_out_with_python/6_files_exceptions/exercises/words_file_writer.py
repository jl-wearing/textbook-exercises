#Program to write words from the user to a file.

#Constants used by the program.
FILE_PATH = 'files/words.txt'

def main():
    """Write words from the user to a file."""
    try:
        #Input number of words to write.
        number_of_words = int(input('Enter the number of words: '))

        #Open the file for writing.
        output = open(FILE_PATH, 'w')

        #Input
        for num in range(1, number_of_words+1):
            output.write(input(f'Enter word {num}: '))
            output.write('\n')

        #Close the file.
        output.close()
    except ValueError:
        print("Please input numbers!")
    except Exception as err:
        print(f"An error as occurred: {err}")

#Call the main function.
if __name__ == '__main__':
    main()