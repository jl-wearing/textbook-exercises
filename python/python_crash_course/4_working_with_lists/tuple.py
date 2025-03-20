#A tuple is an immutable list of items.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#If you want a tuple with only 1 element, you need to include a trailing comma.
my_t = (3,)
print(my_t[0])

#You can use a for loop to traverse all elements in a tuple.
for dimension in dimensions:
    print(f"Dimension of rectangle: {dimension}")

#You can reassign a variable that references a tuple to a new tuple.
print()
dimensions = (400, 100)
for dimension in dimensions:
    print(f"New Dimension: {dimension}")