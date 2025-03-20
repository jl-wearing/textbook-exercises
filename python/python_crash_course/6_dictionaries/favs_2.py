favorite_languages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'rust',
    'phil': 'Python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi, {name.title()}.")

    if name in friends:
        print(f"\t{name.title()}, I see you love {favorite_languages[name]}!")