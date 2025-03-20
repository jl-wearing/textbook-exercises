#To determine if a number is a multiple of 10.
num = int(input('Enter a number and I will tell you if it is a multiple of 10: '))

#Process & Output
if num % 10 == 0:
    print(f"\nThe number {num} is a multiple of 10.")
else:
    print(f"\nThe number {num} is not a multiple of 10.")