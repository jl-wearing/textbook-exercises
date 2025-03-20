#A list inside a dictionary.
favorite_places = {
    'len': ['thailand', 'bali', 'japan'],
    'tom': ['mauritius', 'fort lauderdale', 'cape town'],
    'ahmed': ['baghdad', 'palestine', 'riyadh']
}


for name, list in favorite_places.items():
    print(f"{name.title()}'s favorite places are: ")
    for place in list:
        print(f"\t{place.title()}")
    print()
    