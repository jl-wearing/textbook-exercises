from pathlib import Path
import json

def get_stored_username(path):
    """Get stored name if available."""
    if path.exists():
        contents = path.read_text()
        name = json.loads(contents)
        return name
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    name = input('What is your name?: ')
    contents = json.dumps(name)
    path.write_text(contents)
    return name

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back.")

#testing
greet_user()