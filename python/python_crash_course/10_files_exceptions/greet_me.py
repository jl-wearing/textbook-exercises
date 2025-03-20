from pathlib import Path
import json

#get a pointer to the file.
path = Path('username.json')

#try to read the contents of the file.
try:
    contents = path.read_text()
except FileNotFoundError:
    pass
else:
    name = json.loads(contents)

    #output
    print(f"Welcome back, {name.title()}.")