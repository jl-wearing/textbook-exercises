glossary = {
    'python': 'A programming language.',
    'list': 'A dynamic data structure that stores values in a particular order.',
    'tuple': 'A data structure that cannot change its size once set.',
    'set': 'A collection of unique items.',
    'dictionary': 'A dynamic structure that makes associations between values.',
    'key': 'The item used to index a value in a dictionary.',
    'value': 'The item stored in a dictionary.'
}

for word, description in glossary.items():
    print(f"{word.title()}")
    print(f"\t{description}\n")
print()