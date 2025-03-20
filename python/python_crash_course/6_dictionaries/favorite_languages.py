#Nesting a list in a dictionary.
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for value in language:
        print(f"\t{value.title()}")
print()