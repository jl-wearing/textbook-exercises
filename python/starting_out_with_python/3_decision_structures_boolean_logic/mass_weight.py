#Program to convert mass to weight.
#weight = mass * 9.8

#Constants
GRAVITATIONAL_CONSTANT = 9.8
UPPER_WEIGHT_BOUND = 500
LOWER_WEIGHT_BOUND = 100

#Input
mass = float(input('Enter mass of object: '))

#Process
weight = mass * GRAVITATIONAL_CONSTANT

if weight > UPPER_WEIGHT_BOUND:
    print("\nObject too heavy.")

if weight < LOWER_WEIGHT_BOUND:
    print("\nObject too light.")