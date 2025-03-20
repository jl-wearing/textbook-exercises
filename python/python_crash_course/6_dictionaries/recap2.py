#A variable is a named storage location.
message = "hello"
print(message)
print()

#Data is separated into different types because we wish to
#perform different operations on that data.
#A string is a sequence of characters.

str1 = """This is a string"""
print(str1)
str1 = 'The goal is to read "Hamlet" by tomorrow.'
print(str1)
print()

#Changing case: upper(), lower(), title()
name = "jUstiN"
print(name.upper())
print(name.lower())
print(name.title(), end='\n\n')
#A method is an action that can be performed on a piece of data.

first_name = "justin"
last_name = "wearing"
print(f"{first_name.title()} {last_name.title()}")
full_name = f"{first_name} {last_name}"
print(f"My name is {full_name.title()}\n")

#Whitespace refers to any non-printing characters.
#Stripping whitespace: lstrip(), rstrip(), strip()
word = "      ***word***       "
print(f"{word.rstrip()}")
print(f"{word.lstrip()}")
print(f"{word.strip()}\n")

#Removing prefixes and suffixes: removeprefix(), removesuffix()
url = "www.google.com"
file_name = "notes.txt"
print(f"{url.removeprefix("www.")}")
print(f"{file_name.removesuffix(".txt")}\n")

#When writing large numbers, you can make them more readable by placing underscores
num = 1_000_000_000
print(num, '\n')
#You can assign values to more than one variable in a single line of code.
num, sums = 1_123_456, 0.1_000_123
print(num, sums, '\n')
#A constant is a value that does not change throughout the life of a program.
#Python convention is to capitalize variable names that refer to constants.
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS, '\n')

#A list is a homogeneous, dynamic data strucuture.
#A list is a collection of items in a particular order.
bicycles = ['trek', 'redline', 'dunlop']
print(bicycles)
#Elements of a list are accessed by index.
print(bicycles[0])
print(bicycles[-1], '\n')

#Modifying, adding, and removing elements in a list.
#Modifying
players = ['messi', 'ronaldo', 'mbappe', 'hazard', 'trossard', 'mount', 'sterling']
players[-2] = 'cucurella'
print(players)

#Adding
players.append('lukaku')
players.insert(1, 'benzema')
print(players, '\n')

#Removing
del players[-1]
print(players)
removed_player = players.pop(0)
print(f"{removed_player.title()}")
print(players)
players.remove('sterling')
print(players, '\n')

#Organising a list.
cars = ['mercedes', 'bmw', 'toyota', 'audi', 'suzuki', 'honda']
print(cars)
cars.sort()
print(cars)
cars = ['mercedes', 'bmw', 'toyota', 'audi', 'suzuki', 'honda']
cars.sort(reverse=True)
print(cars)
cars = ['mercedes', 'bmw', 'toyota', 'audi', 'suzuki', 'honda']
print(sorted(cars))
print(sorted(cars, reverse=True))
cars.reverse()
print(cars)
cars.reverse()
length = len(cars)
print(f"Number of cars in the garrage: {length}\n")

#Looping through a list.
cars = ['mercedes', 'bmw', 'toyota', 'audi', 'suzuki', 'honda']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print()

#Making numerical lists.
#The range() function is used to generate a series of numbers.
#You can convert the results from range into a list using the list() function.
for i in range(10):
    print(i, end=' ')
print()
list = list(range(10))
print(list)
#The range function can also be used to specify a step size.
list = [num for num in range(0, 11, 2)]     #List comprehension
print(list, '\n')

#The min(), max(), sum() functions operate on lists.
print(min(list))
print(max(list))
print(sum(list), '\n')

#Working with part of a list.
#This is called making a slice.
for car in cars[2:]:
    print(car, end=' ')
print()
for car in cars[:3]:
    print(car, end=' ')
print()
#You can specify a third argument in the brackets.
#It tells python how many items to skip in the range.
players = ['messi', 'mbappe', 'benz', 'modric', 'navas', 'bruno']
print(players[0:-1:2], end=' ')
print()

#Copying a list.
foods = ['lemon', 'icing', 'sugar', 'flour']
copy = foods[:]
print(foods)
print(copy, '\n')

#Lists work well for storing collections of items that can change throughout the life of a program.
#A tuple refers to an immutable list of items. Once defined, a tuple cannot be altered.
dimensions = (100, 50)
print(dimensions)
for num in dimensions:
    print(dimensions)
print()
print(dimensions[0], '\n')

#if statements
age = 16
height = 1.6
if age >= 16 and height >= 1.6:
    print("You qualify for the ride")
else:
    print("You do not qualify.")
print()

usernames = ['japolo', 'kerrigan', 'reynor', 'arcturus', 'zeratul']
name = input('Enter username: ')
if name.lower() in usernames:
    print('Username already taken.')
else:
    print('Username available')
    usernames.append(name.lower())
print()
name = 'marie'
banned_users = ['mrbeast', 'hitler']
if name not in banned_users:
    print('Awaiting response')
print()

#Checking that a list is not empty.
#If the name of a list is used in an if statement, python returns
#true if there is at least one element.
toppings = []
if toppings:
    for topping in toppings:
        print(f"Adding {topping}")
else:
    print("Are you sure you want a plain pizza?")
print()