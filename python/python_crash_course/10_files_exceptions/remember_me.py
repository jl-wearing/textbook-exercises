from pathlib import Path
import json

#input
name = input('What is your name?: ')

path = Path('username.json')
contents = json.dumps(name)
path.write_text(contents)

#output
print("We'll remember you when you come back.")