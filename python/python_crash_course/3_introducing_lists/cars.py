#You can sort the elements in a list using the sort() method.
cars = ['toyota', 'subaru', 'audi', 'bmw']
print(f"Before Sort: {cars}.")
cars.sort()
print(f"After Sort:  {cars}.")

#Sorting results in a permanent change to the list and it cannot be reversed.
#To sort in reverse order:
cars.sort(reverse = True)
print(f"Reverse Sort: {cars}.")

cars = ['toyota', 'subaru', 'audi', 'bmw']
print()

#You can use the sorted() function to temporarily sort a list.
print(f"Original List: {cars}.")
print(f"Temporarily Sorted List: {sorted(cars, reverse=True)}.")
print(f"Original List: {cars}.")

#You can reverse the order of a list using the reverse() method.
print()
print(cars)
cars.reverse()
print(f"In reverse order: {cars}.")

#The len() function is used to find the length of a list.
length = len(cars)
print(f"The length of the list of cars {cars} is {length} elements.")