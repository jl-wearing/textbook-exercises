#Program to read numbers from a file and perform math operations on them.

file_name = r"files\numbers.txt"

def calculate_sum():
    """Calculate the sum of numbers in a file."""
    #Open the file for reading.
    my_file = open(f'{file_name}', 'r')

    #Determine the total.
    total = 0
    for line in my_file:
        total+= int(line)

    #Close the file.
    my_file.close()

    return total

def calculate_average():
    """Calculate the average of numbers in a file."""
    #Open the file for reading.
    my_file = open(f"{file_name}")

    #Determine the total and count the number of lines.
    total = count = 0
    for line in my_file:
        count+=1
        total+= int(line)

    #Close the file.
    my_file.close()

    return total / count

def get_max():
    """Determine the largest number in a file."""
    #Open the file for reading.
    my_file = open(f"{file_name}")

    #Determine the largest number.
    largest = int(my_file.readline())
    for line in my_file:
        if int(line) > largest:
            largest = int(line)

    return largest

def get_min():
    """Determine the smallest number in a file."""
    # Open the file for reading.
    my_file = open(f"{file_name}")

    # Determine the largest number.
    smallest = int(my_file.readline())
    for line in my_file:
        if int(line) < smallest:
            smallest = int(line)

    return smallest

def main():
    """Mainline logic for the math operations program."""
    #Determine the largest number in the file.
    largest = get_max()

    #Determine the smallest number in the file.
    smallest = get_min()

    #Determine the sum of the numbers in the file.
    total = calculate_sum()

    #Determine the average of the numbers in the file.
    average = calculate_average()

    #Output
    print(f"Largest: {largest:<}")
    print(f"Smallest: {smallest:<}")
    print(f"Total: {total:<}")
    print(f"Average: {average:<.2f}")

#Call the main function.
if __name__ == '__main__':
    main()