#Program to determine which rectangle has a greater area.

#Input
length1 = float(input('Enter the length of rectangle 1: '))
width1 = float(input('Enter the width of rectangle 1: '))
length2 = float(input('Enter the length of rectangle 2: '))
width2 = float(input('Enter the width of rectangle 2: '))

#Process
area1 = length1 * width1
area2 = length2 * width2

#Output
if area1 > area2:
    print(f"\nRectangle 1 has a greater area than rectangle 2.")
    print(f"{area1:.2f} > {area2:.2f}")
elif area1 < area2:
    print(f"\nRectangle2 has a greater area of rectangle 1.")
    print(f"{area2:.2f} > {area1:.2f}")
else:
    print(f"\nThe rectangles have the same area of {area1:.2f} units^2.")