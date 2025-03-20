from pathlib import Path
import json

user = {
    'first': 'lionel',
    'last': 'messi',
    'age': 45,
    'occupation': 'footballer',
}

path = Path('user.json')
contents = json.dumps(user)
path.write_text(contents)