favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

names = ['jen', 'tom', 'kale', 'phil', 'thorfinn']
for name in names:
    if name in favorite_languages.keys():
        print(f"Thank you for taking the poll, {name.title()}.")
    else:
        print(f"{name.title()}, you are invited to take the poll.")
print()