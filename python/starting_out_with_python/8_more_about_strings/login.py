"""Module to generate a login name for students in a university campus."""

def get_login_name(first_name, last_name, student_id):
    """Determine the login name for a student."""
    # Process.
    login_name = first_name[:3] + last_name[:3] + student_id[-3:]

    return login_name

def get_credentials():
    """Get the student's details."""
    # Get the first & last name from the student.
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')

    # Get the student ID from the student.
    student_id = input('Enter your student id: ')

    return first_name, last_name, student_id

def get_student_password():
    """Get a student's login password."""
    print("\nYour password should meet the following criteria: ")
    print('- at least 1 uppercase character')
    print('- at least 1 lowercase character')
    print('- at least 1 digit,')
    print('- and have a length of 7 or greater')
    password = input('Please enter a password: ')

    return password

def validate_password(password):
    """Determine if the student's password is valid."""
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    if len(password) >= 7:
        correct_length = True

    for character in password:
        if character.islower():
            has_lowercase = True
        if character.isupper():
            has_uppercase = True
        if character.isdigit():
            has_digit = True

    return correct_length and has_digit and has_lowercase and has_uppercase


def main():
    """Mainline logic for determining a student's login name."""
    # Get the student's credentials.
    first_name, last_name, student_id = get_credentials()

    # Determine the student's login name.
    login_name = get_login_name(first_name, last_name, student_id)

    # Prompt student for a valid password.
    while True:
        # Get password as input.
        password = get_student_password()

        # Validate the password.
        is_valid = validate_password(password)
        if is_valid:
            break

    # Output
    print(f"\nYour system login name is: {login_name}")
    print(f"Your password is: {password}")

# Call the main function.
if __name__ == '__main__':
    main()