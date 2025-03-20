from sorting import insertionSort
from sorting import bubbleSort

# Testing the functions
arr = [5, 8, 3, 2, 87, 9, 7, 3, 5, 7, 34, 6, 356, 27, 753, 4634, 752, 2, 6, 8, 9, 0, 1, 135, 463]
print("Original:", arr)

insertionSort(arr)
print("After Insertion Sort:", arr)

arr = [5, 8, 3, 2, 87, 9, 7, 3, 5, 7, 34, 6, 356, 27, 753, 4634, 752, 2, 6, 8, 9, 0, 1, 135, 463]
bubbleSort(arr)
print("After Bubble Sort:", arr)

arr = [5, 8, 3, 2, 87, 9, 7, 3, 5, 7, 34, 6, 356, 27, 753, 4634, 752, 2, 6, 8, 9]