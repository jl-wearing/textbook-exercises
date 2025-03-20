from pathlib import Path
import json

path = Path('username.json')
if path.exists():
    #read the username.
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}")
else:
    #write a username.
    name = input('What is your name?: ')
    contents = json.dumps(name)
    path.write_text(contents)