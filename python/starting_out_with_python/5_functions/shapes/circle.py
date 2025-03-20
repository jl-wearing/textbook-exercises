"""Module containing functions that perform mathematical calculations with circles."""
import math

def calculate_area(radius):
    """Calculate the area of a circle."""
    try:
        area = math.pi * radius**2
    except TypeError:
        print("Error! Enter a valid number.")
    else:
        return area

def calculate_circumference(radius):
    """Calculate the circumference of a circle."""
    try:
        circumference = 2 * math.pi * radius
    except TypeError:
        print("Error! Enter a valid number.")
    else:
        return circumference