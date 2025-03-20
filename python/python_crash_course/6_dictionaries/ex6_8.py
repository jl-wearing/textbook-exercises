names = ['jen', 'justin', 'sarah', 'messi']
pet_list = ['cat', 'fish', 'dog', 'pigeon']
pet_list.sort()

pets = []
for i in range(len(names)):
    pet = {
        f'{names[i]}': f'{pet_list[i]}',
    }

    pets.append(pet)

#Display data about pets.
for dictionary in pets:
    for name, pett in dictionary.items():
        print(f"Name: {name.title()}")
        print(f"Animal: {pett.title()}\n")