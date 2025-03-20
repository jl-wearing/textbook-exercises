#Looping through all key-value pairs.
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
print()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite programming language is {language.title()}.")
print()
#Looping through all key value pairs works well for dictionaries that store the same
#kind of information for many objects.

#Looping through all the keys in a dictionary.
#The keys() method is used to retrieve the keys in a dictionary.
for name in favorite_languages.keys():
    print(f"Name : {name.title()}")
print()

#Looping through the keys is the default behaviour for the for loop, 
#thus the keys() method is not required.
friends = ['phil', 'sarah']
for name in favorite_languages:
    print(f"Hi {name.title()}")
    if name in friends:
        print(f"\t{name.title()}, I see you love {favorite_languages[name].title()}!")
print()

#To determine if erin took the poll.
if 'erin' not in favorite_languages.keys():
    print("Erin, please take the poll!")
print(favorite_languages.keys(), '\n')

#Looping through the keys in a particular order.
#Looping through a dictionary returns the items in the same order they were inserted.
for name in sorted(favorite_languages.keys()):
    print(f"Thank you, {name.title()}, for taking the poll.")
print()

#Looping through the values in a dictionary.
print(favorite_languages.values())
print("The following programming languages were mentioned: ")
for language in set(favorite_languages.values()):
    print(f"{language.title()}")
print()

#A set is a collection in which each item is unique.
#The set function returns a collection of unique elements.
#You can build a set using braces and separating each element with commas.
set_of_languages = {language for language in favorite_languages.values()}
print(set_of_languages)
#Unlike dictionaries and lists, sets do not retain items in any specific order.