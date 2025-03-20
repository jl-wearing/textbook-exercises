#The min() function returns the smallest element in a list.
#The max() function returns the largest element in a list.
#The sum() function returns the sum of all elements in a list.

numbers = list(range(5, 50, 5))
print(numbers)
print()

lowest = min(numbers)
highest = max(numbers)
sum = sum(numbers)

#Output
print(f"Smallest element: {lowest}.")
print(f"Largest element: {highest}.")
print(f"Sum: {sum}.")