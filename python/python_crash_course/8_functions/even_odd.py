#Even and odd functions.

def even(num):
    """Function to determine if a number is even."""
    return num % 2 == 0

def odd(num):
    """Function to determine if a number is odd."""
    return num % 2 != 0

#Testing the functions.
num = int(input('Enter a number: '))
if(even(num)):
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")