import random

#To produce a list of square numbers.
squares = [i*i for i in range(1, 11)]

#To produce a list of even numbers using list comprehensions.
bool_evens = [(i % 2 == 0) for i in range(1, 21)]
evens = []
i = 1
for element in bool_evens:
    if element:
        evens.append(i)
    i+=1

#To produce a list of cubes numbers.
cubes = [i**3 for i in range(1, 11)]

#Output
print(squares, cubes, evens, sep='\n')

#Output the lengths of each string in the list.
str_list = ['Winken', 'Blinken', 'Nod']
lens = [len(string) for string in str_list]
print(lens)

#Using if clauses with list comprehensions.
data = []
for i in range(10):
    data.append(random.randint(1, 20))
#Making a new list with elements < 10.
less_10 = [num for num in data if num < 10]
print('\n',data)
print(less_10)