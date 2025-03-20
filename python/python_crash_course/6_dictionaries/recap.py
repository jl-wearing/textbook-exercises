#Changing case
str = "heLLo world"
print(str.lower())
print(str.title())
print(str.upper())
print()

#f-strings
f_name = "ada"
l_name = "lovelace"
full_name = f"{f_name} {l_name}"
print(full_name)
print()

#Stripping whitespace.
str = "      hello"
print(f"Before stripping: {str}")
print(f"After stripping: {str.lstrip()}")
str = "hello         "
print(str)
print(str.rstrip())
str = "      hello     "
print(str)
print(str.strip())
print()

#Removing prefixes and suffixes.
url = "https://www.google.com"
file_name = "data.txt"
print(f"Prefix removed: {url.removeprefix("https://")}")
print(f"Suffix removed: {file_name.removesuffix(".txt")}")
print()

#Grouping large numbers using underscores.
universe_age = 14_000_000_000
x,y,z = 1,2,3
print(x,y,z)
print(universe_age)
print()

#Lists
bicycles = ['dunlop', 'trek', 'redline', 'specialized']
print(bicycles)
for bicycle in bicycles:
    print(bicycle,end=' ')
print()
print(bicycles[0].upper(), bicycles[-1], bicycles[-2])
print(f"My first bicycle was a {bicycles[0].title()}.")
print()

#Modifying, adding, & removing elements.
bicycles[0] = 'honda'       #modify
print(bicycles)
bicycles.append('suzuki')   #add to end
print(bicycles)
bicycles.insert(1, 'bmw')   #add to any position
print(bicycles)
del bicycles[2]             #remove according to position
print(bicycles)
last_bike = bicycles.pop()  #remove the last element
print(f"Last bike: {last_bike}")
print(bicycles)
print()
#pop() can also remove any item by specifying an index.

#remove() removes the first occurrence of the specified element.
motorcycles = ['ducati', 'bmw', 'suzuki', 'kawasaki', 'honda']
motorcycles.remove('suzuki')
print(motorcycles)
print()

#Sorting Lists.
cars = ['toyota', 'honda', 'mercedes', 'bmw', 'hyundai', 'audi']
print(cars)
cars.sort()                 #sorts a list permanently in alphabetical order
print(cars)
cars = ['toyota', 'honda', 'mercedes', 'bmw', 'hyundai', 'audi']
cars.sort(reverse=True)     #sorts a list in reverse order permanently in alphabetical order.
print(cars)
cars = ['toyota', 'honda', 'mercedes', 'bmw', 'hyundai', 'audi']
print(sorted(cars))         #sorts a list temporarily
print(sorted(cars, reverse=True))
cars.reverse()              #reverses the order of a list permanently.
print(cars)
print()

#Length of a list.
cars = ['toyota', 'honda', 'mercedes', 'bmw', 'hyundai', 'audi']
number_of_cars = len(cars)
print(f"Number of cars in garrage: {number_of_cars}.")
print()

#Looping
magicians = ['alice', 'david', 'shawn']
for magician in magicians:
    print(magician, end=' ')
#If you indent a line that doesn't need to be indented, python informs you about the unintended indent.
print()

#Numerical Lists.
for value in range(1,5):        #You specify the first value you want and the first value you don't want.
    print(value, end=' ')
print()
for value in range(6):
    print(value, end=' ')
print()
numbers = list(range(10))       #You can convert the results of range() into a list using the list() function.
print(numbers)
#Passing a third argument to range() specifies a step size.
evens = list(range(2, 11, 2))
print(evens)
squares = []
for value in range(1, 11):
    squares.append(value * value)
print(squares)
print()

#min, max, sum
nums = [1, 3, 54, 534, 4, -45, 324, 563, 562, -34, -674]
print(min(nums))
print(max(nums))
print(sum(nums))

#List Comprehensions
cubes = [value**3 for value in range(1, 11)]
print(cubes)
print()

#Working with part of a list.
#You can work with a specific group of items in a list, called a slice.
players = ['messi', 'ronaldo', 'kroos', 'vinicius']
print(players[0:3])
#If you omit the first index, python starts the slice at the beginning of the list.
print(players[:2], players[2:], players[-3:], sep='\n')
#Passing a third argument specifies a step size.
players = ['messi', 'ronaldo', 'kroos', 'vinicius', 'mbappe', 'mount', 'cucurella', 'enzo', 'palmer']
print(players[:-1:2])
print("First 3 players: ")
for player in players[0:3]:
    print(player, end=' ')
print(f'\n\n')

#Copying a list.
foods = ['lemon', 'icing', 'sugar', 'flour']
copy = foods[:]
print(foods, copy, sep='\n')

#Tuples.
#A tuple is an immutable list.
dimensions = (200, 50)
print(dimensions)
print(dimensions[0], dimensions[1])
for value in dimensions:
    print(value, end=' ')
print()