# Program to determine if an account number in a file is valid.

# Constants used by the program.
FILE_NAME = "charge_accounts.txt"

def get_account_number_input():
    """Get the account number to search for from the user."""
    account_number = input('Enter the account number to search for: ')
    return account_number

def search_file_for_account_number(account_number):
    """Search the file for the specified account number."""

    # Open the file for reading.
    infile = open(FILE_NAME, 'r')

    # Store the contents of the file in a list.
    file_contents = infile.readlines()

    # Close the file.
    infile.close()

    # Remove the \n from each word number in the list.
    for index in range(len(file_contents)):
        file_contents[index] = file_contents[index].rstrip('\n')

    # Determine if the account number is in the list.
    if account_number in file_contents:
        print(f"Account number {account_number} is valid.")
    else:
        print(f"Account number {account_number} is invalid.")

def main():
    """Mainline logic for searching for account numbers."""
    prompt = "\nEnter an account number to search for or enter 'q' to quit: "
    while True:
        # Get the account number from the user.
        account_number = input(prompt)

        if account_number == 'q':
            break

        search_file_for_account_number(account_number)

# Call the main function.
if __name__ == '__main__':
    main()