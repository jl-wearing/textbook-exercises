#Function to return the sum of numbers from 1 to n.

def sum(n):
    """Recursive definition of summation."""
    if n <= 1:
        return n
    else:
        return n + sum(n - 1)
    
def summate(n):
    """Iterative definition of summation."""
    count = n
    sum = 0
    while count > 0:
        sum+= count
        count-= 1
    return sum

#Testing the functions.
summation = sum(10)
print(f"Summation from 1 to 10: {summation}.\n")

summation = summate(10)
print(f"Summation from 1 to 10: {summation}.\n")