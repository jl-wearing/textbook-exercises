#Program to get employee data from the user and save it to a file.

def main():
    """Mainline logic for saving employee records to a file."""
    #Get the number of employee records to create.
    while True:
        try:
            number_of_records = int(input('How many employee records '
                                          'do you wawnt to create?: '))
            break
        except ValueError:
            print("Please enter valid numerical data.")

    #Open a file for writing.
    output = open('files/employees.txt', 'w')

    #Write employee records to the file.
    for num in range(1, number_of_records+1):
        #Get employee data from the user.
        name = input('\nEnter employee name: ')
        id_number = input('Enter id number: ')
        dept = input('Enter department name: ')

        #Write data to the file.
        output.write(name.title() + '\n')
        output.write(id_number + '\n')
        output.write(dept.title() + '\n')

    #Close the file.
    output.close()

#Call the main function.
if __name__ == '__main__':
    main()