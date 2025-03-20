#Program to determine if a number is positive or negative.

#Input
num = int(input('Enter a number: '))

#Process and Output
if num < 0:
    print(f"\n{num} is negative.")
elif num > 0:
    print(f"\n{num} is positive.")
else:
    print(f"{num} is zero.")