#Program to sum the numbers in a file.

def main():
    """Simple program to total the numbers in a file."""
    try:
        #Input filename.
        file_name = input('Enter the filename to read: ')

        #Open the file for reading.
        infile = open(file_name, 'r')

        #Process data
        total = 0
        for line in infile:
            total+= int(line)

        #Close the file.
        infile.close()

        #Output
        print(f"\nTotal: {total}")

    except FileNotFoundError:
        print("The file does not exist!")
    except Exception as err:
        print(f"An error has occurred: {err}")

#Call the main function.
if __name__ == '__main__':
    main()