#Program to display lines and their order in a file.

def main():
    try:
        #Input
        file_name = input('Enter filename to read: ')

        #Open the file.
        infile = open(file_name, 'r')

        #Read the contents of the file line by line.
        line_number = 1
        for line in infile:
            print(f"{line_number}: {line.rstrip("\n")}")
            line_number+= 1

        #Close the file.
        infile.close()
    except FileNotFoundError:
        print("The file does not exist!")
    except Exception as err:
        print(err)
        print("An error has occurred.")

#Call the main function.
if __name__ == '__main__':
    main()