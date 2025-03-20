#Program to read from a file and display its contents.

def main():
    """Simple program to read from a file and display its contents."""
    #Open the file for reading.
    my_file = open('files/customers.txt', 'r')

    #Display contents of the file.
    for line in my_file:
        print(line.rstrip('\n').title())

    #Close the file.
    my_file.close()

#Call the main function.
if __name__ == '__main__':
    main()