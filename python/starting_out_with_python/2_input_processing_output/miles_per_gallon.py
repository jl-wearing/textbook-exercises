#Program to calculate the miles per gallon of a car.
#MPG = Miles Driven / Gallons of Gas used.

#Input
miles_driven = float(input('Enter the number of miles driven: '))
gallons = float(input('Enter the number of gallons used: '))

#Process
miles_per_gallon = miles_driven / gallons

#Output
print(f"Miles per gallon: {miles_per_gallon:.2f}.\n")