#Program to output the average of values form data in a file.

def main():
    """
    Simple program to calculate the average of data read
    from a file.
    """
    try:
        #Input filename.
        file_name = input('Enter the filename: ')

        #Open the file for reading.
        infile = open(file_name, 'r')

        #Process data.
        total = 0
        number_of_lines = 0
        value = infile.readline()
        while value != '':
            number_of_lines+= 1
            total+= int(value)

            #Get the next value.
            value = infile.readline()

        #Close the file.
        infile.close()

        #Output
        print(f"\nAverage: {total / number_of_lines:.2f}.")

    except FileNotFoundError:
        print("The file does not exist!")
    except Exception as err:
        print(f"An error has occurred: {err}")

#Call the main function.
if __name__ == '__main__':
    main()