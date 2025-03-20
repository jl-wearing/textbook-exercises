from pathlib import Path
import json

def insert_info(path):
    """Insert user information."""
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')

    while True:
        try:
            age = int(input('Enter your age: '))
        except ValueError:
            print(f"Age cannot be a character!")
        else:
            break
    information = {'first': first_name, 'last': last_name, 'age': age}

    #store the data.
    contents = json.dumps(information)
    path.write_text(contents)

def get_info():
    """Retrieve user information."""
    path = Path('dictionary.json')
    if path.exists():
        #retrieve the user's information
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def display_info():
    """Display a user's information."""
    user_info = get_info()

    if user_info:
        for key, value in user_info.items():
            if key != 'age':
                print(f"{key.title()}: {value.title()}")
            else:
                print(f"{key.title()}: {value}")
    else:
        insert_info(path=Path('dictionary.json'))
        print(f"We'll remember your data for the next time you log in.")

display_info()