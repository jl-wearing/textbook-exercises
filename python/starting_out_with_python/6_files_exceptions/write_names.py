#Program to get 3 names as input and write them to a file.

def main():
    """Simple program to write 3 names to a file."""
    #Open the file for writing.
    my_file = open('files/names.txt', 'w')

    #Get 3 names from the console.
    name_1 = input('Enter first name: ')
    name_2 = input('Enter second name: ')
    name_3 = input('Enter third name: ')

    #Write the names to the file.
    my_file.write(name_1 + '\n')
    my_file.write(name_2 + '\n')
    my_file.write(name_3 + '\n')

    #Close the file.
    my_file.close()

#Call the main function.
if __name__ == '__main__':
    main()