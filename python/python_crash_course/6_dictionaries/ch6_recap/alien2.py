alien_0 = {'x_cor': 0, 'y_cor': 25, 'speed': 'medium'}
print(f"Alien's current position: {alien_0['x_cor']}.\n")

#Move the alien to the right.
#Determine how far to move the alien depending on its speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien.
    x_increment = 3

#The new position is the old position plus the increment.
alien_0['x_cor'] = alien_0['x_cor'] + x_increment
print(f"Alien's new position: {alien_0['x_cor']}.\n")