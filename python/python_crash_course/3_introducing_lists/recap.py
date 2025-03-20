#A list is a dynamic data structure that can hold data of different types.
games = ["cod", "tom clancy", "gta", "nfs"]

#To modify one of the elements.
games[1] = "csgo"
print(games)

#To add new elements.
games.append("valorant")
games.insert(0, "pokemon")
print(games)

#To remove elements
del games[0]
gta = games.pop(-3)
print(gta)
print(games)
games.remove("nfs")
print(games)

#To sort a list
print()
print(sorted(games))
print(sorted(games, reverse=True))
games.reverse()
print(games)
games.sort()
print(games)
games.sort(reverse=True)
print(games)

#The length of the list.
print(f"Number of games: {len(games)} games.")