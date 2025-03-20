#Python functions can also return collections, such as a dictionary.

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}

    return person

def build_person_optional_arguments(first_name, last_name, age=None, occupation=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}

    if age:
        person['age'] = age
    if occupation:
        person['occupation'] = occupation

    return person

#Testing the build_person() function.
musician = build_person('jimi', 'hendrix')
print(musician)
print()

#Testing the build_person_optional_arguments()
user = build_person_optional_arguments('justin', 'wearing', 23, 'student')
print(user)
user = build_person_optional_arguments('kiwi', 'doggo', occupation='sleep all day')
print(user)