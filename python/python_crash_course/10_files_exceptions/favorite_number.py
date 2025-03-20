from pathlib import Path
import json

def get_favorite_number(path):
    """Retrieve a user's favorite number."""
    if path.exists():
        contents = path.read_text()
        fav_num = json.loads(contents)
        return fav_num
    else:
        return None

def insert_favorite_number(path):
    """Insert a person's favorite number, provided they do not have one already."""
    try:
        fav_number = int(input('What is your favorite number: '))
    except ValueError:
        print(f"A character cannot be a favourite number.")
    else:
        contents = json.dumps(fav_number)
        path.write_text(contents)
        print(f"We'll remember your favorite number for next time.")

def display_favorite_number():
    """Get a user's favorite number."""
    path = Path('favorite.json')
    fav_num = get_favorite_number(path)
    if fav_num:
        print(f"I know your favorite number! It's {fav_num}.")
    else:
        insert_favorite_number(path)

#testing
display_favorite_number()