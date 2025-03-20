pets = ['cat', 'dog', 'goldfish', 'dog', 'cat', 'cat', 'pigeon', 'dove']

#We can use a while loop to remove all instances of a value in a list.
while 'cat' in pets:
    pets.remove('cat')

#Confirm all instances of cat were removed.
print(pets)