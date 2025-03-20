#Giving an imported function an alias.

from sorting import selectionSort as ss

arr = [1,45,5346,6242,3465,234,654,34536,3434235,23423,64234,54,523424235,53423523,42]
print(f"Before sorting: {arr}")
ss(arr)
print(f"After sorting: {arr}")