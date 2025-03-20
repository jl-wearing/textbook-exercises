#A function can return any kind of information you need it to,
#including data structures like lists and dictionaries.

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name.title(), 'last': last_name.title()}
    return person

#Testing the function.
musician = build_person('jimi', 'hendrix')
print(musician)

#Including age, occupation as optional arguments.
def build_2(first_name, last_name, age=None, occupation=''):
    """Return a dictionary of information about a person."""
    if age and occupation:
        person = {'first': first_name.title(), 'last': last_name.title(), \
                   'age': age, 'occupation': occupation.title()}
    elif age and not occupation:
        person = {'first': first_name.title(), 'last': last_name.title(), \
                  'age': age}
    elif occupation and not age:
        person = {'first': first_name.title(), 'last': last_name.title(), \
                  'occupation': occupation.title()}
    else:
        person = {'first': first_name.title(), 'last': last_name.title()}
    
    return person


#Testing the function.
user = build_2('lionel', 'messi', 39, 'footballer')
print(user, '\n')

user = build_2('justin', 'wearing')
print(user, '\n')

user = build_2('kiwi', 'doggy', 7)
print(user, '\n')

user = build_2('ziggy', 'doggy', occupation='guard dog')
print(user, '\n')