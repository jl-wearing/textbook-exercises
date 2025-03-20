#If the key you ask for doesn't exist, you will get a KeyError.
#The solution is to use the get() method to set a default value that will be returned if the 
#specified key does not exist.

alien_0 = {'color': 'green', 'speed': 'slow'}
points_value = alien_0.get('points', 'No point value assigned.')
print(points_value)