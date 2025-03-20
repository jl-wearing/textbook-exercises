#A dictionary can be used to store related information about a single object.
person_1 = {
    'first_name': 'justin',
    'last_name': 'wearing',
    'age': 23,
    'city': 'gaborone',
    }

person_2 = {
    'first_name': 'lionel',
    'last_name': 'messi',
    'age': 45,
    'city': 'miami'
    }

#A list inside a dictionary.
people = [person_1, person_2]
for person in people:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']

    #Output data.
    print(f"First name: {full_name}")
    print(f"Age: {age}\n")