#Program to calculate the circumference & area of a circle.

from math import pi

#Input
radius = float(input('Enter the radius of the circle: '))

#Process
circumference = 2 * pi * radius
area = pi * radius ** 2

#Output
print(f"\nCircumference: {circumference:.2f} units.")
print(f"Area: {area:.2f} units^2.\n")