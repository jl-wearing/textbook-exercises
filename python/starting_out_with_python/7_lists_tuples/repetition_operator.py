#The repetition (*) operator makes copies of a list and joins them together.

numbers = [0] * 5
nulls = [None] * 10

print(numbers, nulls, sep='\n')

numbers = [1,2,3] * 3
print(numbers)

numbers.insert(0, 50)
print(numbers)