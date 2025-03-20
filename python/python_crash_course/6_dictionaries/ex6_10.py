#A list inside a dictionary.
favorite_numbers = {
    'len': [69, 420],
    'tom': [42069, 69420],
    'ahmed': [666, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
}

for name, list in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are: ")
    for number in list:
        print(f"\t{number}")
