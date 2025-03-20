def count_lines(path):
    """Count the number of lines in a file."""
    #Open the file for reading.
    infile = open(path, 'r')

    #Count the number of lines in the file.
    count = 0
    for line in infile:
        count+=1

    #Close the file.
    infile.close()

    return count

def main():
    """Mainline logic for displaying the contents of a file."""

    try:
        #Get the filename from the user.
        file_name = input('Enter the filename: ')

        #Open the file for reading.
        infile = open(file_name, 'r')

        #Get the number of lines in the file.
        number_of_lines = count_lines(file_name)

        if number_of_lines < 5:
            #Retrieve all the data from the file.
            contents = infile.read()

            #Output the data.
            print(contents)
        else:
            #Display ony the first 5 lines.
            for i in range(5):
                print(infile.readline().rstrip('\n'))

        # Close the file.
        infile.close()
    except FileNotFoundError:
        print("File does not exist!")
    except Exception as err:
        print(err)
        print("An error has occurred.")

#Call the main function.
if __name__ == '__main__':
    main()