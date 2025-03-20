def main():
    """Simple program to write data to an output file."""
    #Open a file for writing.
    customer_names = ['Mariah Carey', 'Michael Gambon', 'Simon Cowell']
    customer_file = open('files/customers.txt', 'w')

    #Write the names to the file.
    for name in customer_names:
        customer_file.write(name + '\n')

    #Close the file.
    customer_file.close()

#Call the main function.
if __name__ == '__main__':
    main()