glossary = {
    'list': 'a collection of items of a particular order.',
    'tuple': 'an immutable list of items.',
    'dictionary': 'a collection of key-value pairs.',
    'python': 'an interpreted programming language.',
    'if': 'the start of a conditional test.'
}

for word, meaning in glossary.items():
    print(f"{word.title()}:")
    print(f"\t{meaning}\n")
print()