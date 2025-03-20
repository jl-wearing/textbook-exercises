favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

names = ['john', 'sarah', 'cena', 'phil']
for name in names:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for taking the poll!")
    else:
        print(f"{name.title()}, please take the poll!")
print()