from pathlib import Path
import json

path = Path('user.json')
contents = path.read_text()
user = json.loads(contents)

for key, value in user.items():
    if key != 'age':
        print(f"{key.title()}: {value.title()}")
    else:
        print(f"{key.title()}: {value}")