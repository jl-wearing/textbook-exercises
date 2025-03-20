import json
from pathlib import Path

path = Path('numbers.json')
content = path.read_text()
numbers = json.loads(content)
print(numbers)