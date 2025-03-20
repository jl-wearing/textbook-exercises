def main():
    """Simple program to read from an input file."""
    #Open the file for reading.
    input_file = open('files/customers.txt', 'r')

    #Read the entire contents of the file.
    contents = input_file.read()

    #Close the file.
    input_file.close()

    #Display the file contents.
    print(contents)

    data = contents.splitlines()
    print(data)

#Call the main function.
if __name__ == '__main__':
    main()