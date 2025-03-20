def main():
    """Program to read the contents of a file, line by line."""
    #Open a file for reading.
    input_file = open('files/customers.txt', 'r')

    #Read the contents of the file.
    cust_1 = input_file.readline()
    cust_2 = input_file.readline()
    cust_3 = input_file.readline()

    #Close the file.
    input_file.close()

    #Output.
    print(cust_1, end='')
    print(cust_2, end='')
    print(cust_3, end='')

#Call the main function.
if __name__ == '__main__':
    main()