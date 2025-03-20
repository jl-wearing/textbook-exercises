#Program to read and display employee records from a file.

def main():
    """Mainline logic for reading and displaying employee records."""
    #Open a file for reading.
    try:
        infile = open('files/employees.txt', 'r')
    except FileNotFoundError:
        print("File Not Found!")

    #Read records from the file and store in a list.
    employees = []
    while True:
        #Potential name
        name = infile.readline()

        #If we are at the end of the file.
        if name == '':
            break

        #Read the rest of the employee records.
        name = name.rstrip('\n')
        id_number = infile.readline().rstrip('\n')
        dept = infile.readline().rstrip('\n')

        employee_information = {
            'name': name.title(),
            'id': id_number,
            'department': dept.title()
        }
        employees.append(employee_information)

    #Output the employee records.
    for employee in employees:
        for key, value in employee.items():
            print(f"{key.title()}: {value.title()}")
        print()

#Call the main function.
if __name__ == '__main__':
    main()