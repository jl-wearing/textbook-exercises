#Python functions can accept an arbitrary number of keyword arguments.
#The return type is a dictionary.

def build_profile(first, last, **user_info):
    """
    Display the dictionary of information about a person.
    :param first: the first name
    :param last: the last name
    :param user_info: the dictionary of information about a person
    :return: the dictionary of information about a person.
    """
    user_info['first'] = first
    user_info['last'] = last

    return user_info

#Testing the build_profile() function.
user =build_profile('albert', 'einstein', age=100, location='princeton', field='physics')
for key, value in user.items():
    if key != 'age':
        print(f"{key.title()}: {value.title()}")
    else:
        print(f"{key.title()}: {value}")
print()
print(user)