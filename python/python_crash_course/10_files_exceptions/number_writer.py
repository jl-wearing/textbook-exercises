from pathlib import Path
import json

evens = list(range(2, 22, 2))
path = Path('numbers.json')
contents = json.dumps(evens)
path.write_text(contents)