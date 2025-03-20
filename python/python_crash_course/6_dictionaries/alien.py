#Demonstrating the use of a dictionary.
#A dictionary is used to make an association between related information.

alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

new_points = alien_0['points']
print(f"You just earned {new_points} points!\n")

#Adding new key-value pairs.
alien_0['coordinates'] = (0, 25)
print(alien_0['coordinates'])
print(alien_0['coordinates'][0], '\n')        #To access the first element in the tuple.

#Empty dictionary.
empty = {}
print(empty, '\n')

#Modifying the values in a dictionary.
print(f"Alien's color: {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"Alien's new color: {alien_0['color']}.")
print(alien_0, '\n')

#Deleting kev-value pairs in a dictionary.
del alien_0['points']
print(alien_0)