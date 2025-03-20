#Program to append data to the end of a file.

def main():
    """Simple program to append data to a file."""
    #Open the file for writing.
    output_file = open(r'files\customers.txt', 'a')

    #Write to the file.
    output_file.write('Jeremy Clarkson\n')
    output_file.write('James May\n')
    output_file.write('Richard Hammond\n')

    #Close the file.
    output_file.close()

#Call the main function.
if __name__ == '__main__':
    main()