#A dictionary is used to make associations between related information.
#A dictionary is a collection of key-value pairs.
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

points = alien_0['points']
print(f"You earned {points} points!")

#Adding new key-value pairs.
alien_0['x_cor'] = 0
alien_0['y_cor'] = 25
print(alien_0, '\n')

#Dictionaries retain the order in which they were defined.
#You can create an empty dictionary and add key-value pairs later.
#Empty dictionaries are typically used to store user supplied data.

#Modifying values in a dictionary.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['color'] = 'yellow'
alien_0['points'] = 10
print(alien_0)

#Removing key value pairs.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0, '\n')

#Previous examples involved storing different kinds of information about one object.
#You can also use a dictionary to store one kind of information about many objects.

#Using get() to access values.
#Using keys to retrieve a value will raise an error if the key does not exist.
#A solution to this is to use the get() method.
#You can use the get() method to set a default value if the key does not exist.
color_value = alien_0.get('speed', 'No speed was assigned to this alien.')
print(color_value)

#If there's a chance the key might not exist, consider using the get() method instead.
#If you leave out the 2nd argument and the key does not exist, the get() method will return None.