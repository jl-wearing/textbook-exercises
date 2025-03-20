# The process of storing dictionaries inside lists,
# storing lists as value in a dictionary,
# or storing dictionaries inside dictionaries is called nesting.

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print()

#Auto-generate green aliens.
#Make an empty list for storing aliens.
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow',}
    aliens.append(new_alien)
print()

#Display the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print()

#Show how many aliens have been created.
print(f"Number of aliens: {len(aliens)}.")

#Change the first 3 aliens to yellow and speed to medium.
for alien in aliens[:3]:
    if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['points'] = 10
            alien['speed'] = 'medium'
    elif alien['color'] == 'red':
            alien['color'] = 'red'
            alien['points'] = 10
            alien['speed'] = 'fast'
print(aliens[:5])
print()