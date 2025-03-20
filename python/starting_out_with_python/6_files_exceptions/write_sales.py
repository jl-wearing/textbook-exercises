#Program to write sales data to a program.

def get_input():
    """Get the number of data items to be written to the file."""
    while True:
        try:
            number_of_items_to_read = int(input('Enter the amount of'
                                            ' data to read: '))
            break
        except ValueError:
            print("Please enter a valid numerical figure.")

    return number_of_items_to_read

def write_sales_data(file_path, size_of_data):
    """Write sales data to a file."""
    #Open the file for writing.
    my_file = open(rf'{file_path}', 'w')
    for num in range(1, size_of_data + 1):
        #Get sales figure input from the user.
        data = input(f'Enter sales figure #{num}: ')

        #Write the data to the file.
        my_file.write(data + "\n")

    #Close the file.
    my_file.close()

def main():
    """Mainline logic for writing sales data."""
    file_path = "files/sales.txt"

    #Get the number of items to read.
    size_of_data = get_input()

    #Write data to the file.
    write_sales_data(file_path, size_of_data)

#Call the main function.
if __name__ == '__main__':
    main()