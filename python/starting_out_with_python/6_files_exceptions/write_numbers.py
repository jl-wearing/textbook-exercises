#Program to write 3 numbers to a file.

def main():
    """Simple program to write 3 numbers to a file."""
    #Input
    num_1 = int(input('Enter the first number: '))
    num_2 = int(input('Enter the second number: '))
    num_3 = int(input('Enter the third number: '))

    #Open a file for writing.
    output = open(r'files\numbers.txt', 'w')

    #Write data to the file.
    output.write(str(num_1) + '\n')
    output.write(str(num_2) + '\n')
    output.write(str(num_3) + '\n')

    #Close the file.
    output.close()

#Call the main function.
if __name__ == '__main__':
    main()