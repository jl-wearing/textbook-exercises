#Program to manipulate coffee records for a business.

import os

#Global constants for the program.
FILE_PATH = 'files/coffee.txt'

def add_records(number_of_records=1):
    """Add a record to the file."""
    #Open the file for appending.
    output = open(f'{FILE_PATH}', 'a')

    #Write to the file.
    for num in range(1, number_of_records+1):
        #Get input from the user.
        description, quantity = get_input()

        #Append data to file.
        output.write(description.lower() + '\n')
        output.write(quantity + '\n')

    #Close the file.
    output.close()

def get_input():
    """Get coffee description, and quantity from the user."""
    description = input('Enter coffee description: ')
    quantity = input('Enter stock quantity: ')

    return description, quantity

def display_records():
    """Display the records in the file."""
    #Open the file for reading.
    try:
        infile = open(FILE_PATH, 'r')
    except FileNotFoundError:
        print("File Not Found!")

    #Read records from the file.
    description = infile.readline()
    while description != '':
        description = description.rstrip('\n')
        quantity = infile.readline().rstrip('\n')

        #Output
        print(f"\nDescription: {description}")
        print(f"Quantity:      {quantity}")

        #Get the next item to read.
        description = infile.readline()

    #Close the file.
    infile.close()

def search_by_description():
    """Determine if a record exists in the file."""
    #Open the file for reading.
    infile = open(FILE_PATH, 'r')

    #Determine what the description criteria is.
    description = input('What would you like to search for?: ')

    #Check if the description matches any in the file.
    for line in infile:
        if line.lower().rstrip('\n') == description.lower():
            infile.close()
            return True
    infile.close()
    return False

def alter_record():
    """Alter the quantity of a record."""
    #Open input file for reading and temp output file for writing.
    infile = open(FILE_PATH, 'r')
    output = open('files/temp.txt', 'w')

    #Determine the description criteria.
    description = input('What would you like to alter?: ')

    #Copy all content from the read file to the write file.
    #unti we reach the data to be altered.
    data = infile.readline().rstrip('\n')
    while data != '':
        output.write(data.lower() + '\n')
        if data.lower() == description.lower():
            quantity = input('Enter new quantity: ')
            output.write(quantity + '\n')
            infile.readline()
        else:
            output.write(infile.readline())

        #Get the next data item to read.
        data = infile.readline().rstrip('\n')

    #Close the files.
    infile.close()
    output.close()

    #Delete the old file.
    os.remove('files/coffee.txt')

    #Rename the new file.
    os.rename('files/temp.txt', 'files/coffee.txt')

def delete_record():
    """Delete a record from the file."""
    #Get the record to delete from the user.
    record_to_delete = input('Enter the record to delete: ')

    #Open the records file for reading and a temp file for writing.
    infile = open(FILE_PATH, 'r')
    output = open('files/temp.txt', 'w')

    data = infile.readline()
    while data != '':
        if data.lower().rstrip('\n') == record_to_delete.lower():
            #Skip these fields.
            infile.readline()
        else:
            output.write(data)
            output.write(infile.readline())

        #Get the next field to read
        data = infile.readline()

    #Close the files.
    infile.close()
    output.close()

    #Delete the file that was read.
    os.remove(FILE_PATH)

    #Rename the temporary file to the new records file.
    os.rename('files/temp.txt', FILE_PATH)

def main():
    """Mainline logic for the coffee records program."""
    #Add a few records to the file.
    add_records(3)
    print()

    #Display the records that were added to the file.
    display_records()
    print()

    #Search for a record, one that exists, and one that does not exist.
    rec_1 = search_by_description()
    rec_2 = search_by_description()
    print(rec_1)
    print(rec_2)
    print()

    #Alter the five roses record.
    alter_record()
    print()

    #Delete the sumatra record.
    delete_record()

#Call the main function.
if __name__ == '__main__':
    main()