#Previous examples showed that dictionaries can be used to store different kinds of information about one object.
#But they can also be used to store one kind of information about many objects.
favorite_languages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'rust',
    'phil': 'Python',
}
print(favorite_languages, '\n')

#Looping through all key-value pairs.
#The items method retrieves a sequence of key-value pairs.
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite programming language is {language.title()}.")
print()

#Looping through the keys.
#The keys() method is used to retrieve each key.
#The keys() method returns a list of all the keys.
for name in favorite_languages.keys():
    print(name.title())
print()

if 'erin' not in favorite_languages.keys():
    print('Erin, take the poll!')