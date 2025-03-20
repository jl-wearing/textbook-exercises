#A dictionary is an association of key-value pairs.
alien = {'color': 'green', 'height': '3'}

#Looping through the keys.
for key in alien.keys():
    print(f"key: {key}")
print()
for key in alien:
    print(f"key {key}")
print()

#Looping through the values.
for value in alien.values():
    print(f"value: {value}")
print()

#Looping through key-value pairs.
for key, value in alien.items():
    print(f"key-value pair: {key, value}")
print()

#Adding new key-value pairs.
alien['points'] = 5
print(alien)
print()

#Dictionaries retain the order in which they were defined.
#When you print a dictionary, you will see the elements in the order they were added to the dictionary.

#Modifying values in a dictionary.
alien['color'] = 'orange'
print(alien)

#Removing key-value pairs.
del alien['color']
print(alien)
print()

#Previously, dictionaries were used to store different kinds of information about one object,
#but they can also be used to store one type of information about many objects.
favorites = {
    'jen': 'c',
    'sarah': 'python',
    'justin': 'java',
    'colt': 'python',
}
#The get() method is used if you are not sure of the keys in the dictionary.
#If you leave out the 2nd argument & the key doesn't exist, python returns the value None.
print(f"{favorites.get('jen', 'name not in list')}")
print(f"{favorites.get('tim', 'name not in list')}")
print()

#Looping through a dictionary returns the keys in the same order they were inserted.
#You can sort the values in the dictionary.
for name, language in sorted(favorites.items()):
    print(f"{name.title()}'s favorite language: {language.title()}")
print()

#Looping through the values displays repeated values.
#To see each value without repetition, we can use a set.
#A set is a data structure in which each item is unique.
print(favorites)
print('Languages in the poll: ')
for language in set(favorites.values()):
    print(f"{language.title()}")
print()

#The set() function forms a collection of unique items.
#You can build a set directly:
set_1 = {language for language in favorites.values()}
print(set_1)
#Sets do not retain items in any specific order.

#Nesting:
#e.g. - to represent information about different aliens:
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1]
print(aliens)
print()

#It makes sense to have aliens auto generated.
mothership = []
for i in range(10):
    alien = {'color': 'green', 'points': 5}
    mothership.append(alien)
size = len(mothership)
print(f"size of mothership: {size}.\n")

#It is common to store dictionaries in a list when each dictionary contains many kinds of information about one object.