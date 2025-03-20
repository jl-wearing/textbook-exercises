for value in range(1, 5):
    print(value, end=' ')
print()

#The range function is used to generate a sequence of numbers.
for value in range(6):
    print(value, end=' ')
print()

#You can convert the results from range() into a list using the list() function.
numbers = list(range(1, 11))
print(numbers)

#Passing a third argument to the range() function specifies a step size.
even_numbers = list(range(2, 11, 2))
print(even_numbers)