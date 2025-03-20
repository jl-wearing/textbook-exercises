alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

fleet = [alien_0, alien_1, alien_2]

for alien in fleet:
    print(alien)
print()

#Auto-generate aliens and add to fleet.
fleet = []
for i in range(30):
    new_alien = {'color': 'green', 'points': 5}
    fleet.append(new_alien)

#Print the first 5 aliens.
for alien in fleet[:5]:
    print(alien)
print()

#Show how many aliens have been created.
print(f"Number of aliens in fleet: {len(fleet)}\n")

#Change the color of the first 3 aliens.
for alien in fleet[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10

for alien in fleet[:5]:
    print(alien)
print()

#It is common to store a number of dictionaries in a list when each dictionary
#contains many kinds of information about one object.
#For example, you might create a dictionary for each user on a website and
#store individual dictionaries in a list.
#NOTE: all the dictionaries in the list must have a similar structure