#Program to read the contents of a file.

def main():
    """Read and display the contents of a file."""
    try:
        #Get the filename to read from the user.
        file_name = input('Enter the file to read: ')

        #Open the file for reading.
        infile = open(file_name, 'r')

        #Get the contents of the file.
        data = infile.read()

        #Close the file.
        infile.close()

        #Display the contents.
        print(data)
    except FileNotFoundError:
        print(f"Error reading {file_name}.")

#Call the main function.
if __name__ == '__main__':
    main()