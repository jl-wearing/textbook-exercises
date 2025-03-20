players = ['messi', 'ronaldo', 'vinicius', 'mbappe', 'ronaldinho', 'benzema', 'beckham']

#You can work with part of a list called a slice.
print(players[0:3])
#If you omit the starting index, python starts the slice at the beginning of the list.
print(players[:2])
#If you want a slice that includes the end of a list, omit the last index.
print(players[3:])
#To print the last 3 players:
print(players[-3:])
print(players[0:-1:2])
print()

#You can loop through a slice of a list.
print("Here are the first 3 players: ")
for player in players[:3]:
    print(player.title())