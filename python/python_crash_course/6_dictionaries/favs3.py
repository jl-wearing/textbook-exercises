favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

#There are 3 ways to loop through a dictionary.
#The first way is to loop through all key-value pairs.
for name, language in favorite_languages.items():
    print(f"Key: {name}")
    print(f"Value: {language}\n")
print()

#The second way is to loop through all keys.
for key in favorite_languages.keys():
    print(f"Key: {key}")
print()

#Looping through a dictionary returns the items in the same order they were inserted.
#You may choose to sort the keys before looping.
for name in sorted(favorite_languages.keys(), reverse=True):
    print(f"Name: {name.title()}")
print()

#The third way is to loop through all values.
#This is done using the values() method.
for language in favorite_languages.values():
    print(f"Programming language: {language}")
print()

#Looping through the values displays repeated values.
#To remove repetition, we use a set.
#A set is a collection in which each item is unique.
for value in set(sorted(favorite_languages.values())):
    print(value.title())
print()

#A set is a collection of unique items.
set_1 = {'python', 'c', 'rust', 'python'}
print(set_1)