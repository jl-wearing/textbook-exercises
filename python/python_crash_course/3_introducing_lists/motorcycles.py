#To change an element in a list, use the name of the list followed by the index of the element you want to change.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#You can use the append() method to add elements to the end of a list.
motorcycles.append('bmw')
print(motorcycles)

#You can add an element at any position using the insert() method.
motorcycles.insert(1, 'kawasaki')
print(motorcycles)

#You can remove an element from a list if you know its position.
del motorcycles[1]
print(motorcycles)

#The pop() method is used to remove the last element in a list.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
last_popped = motorcycles.pop()
print(motorcycles)
print(last_popped)

print()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f"The last motorcycle I purchased was a {motorcycles.pop().title()}.")
print(f"The first motorcylce I owned was a {motorcycles.pop(0).title()}.")
print(motorcycles)

print()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'suzuki']
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)