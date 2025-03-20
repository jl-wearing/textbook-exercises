#Introducing lists.
#A list is a collection of items in a particular order.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Indexing starts from zero.
print(bicycles[0])

#You can also use methods on the elements of a list.
print(bicycles[1].upper())

#The index -1 returns the last element in the list.
print(bicycles[-1])

#You can use individual values from a list just as you would any other variable.
message = f"My first bicycle was {bicycles[2].title()}."
print(message)