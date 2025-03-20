"""Module for calculating an employee's pay."""

MINIMUM_HOURS = 40
OVERTIME_PAY = 10.00
TAX_RATE = 0.14

def get_hours():
    """Get the number of hours worked."""
    hours_worked = float(input('Enter the number of hours worked: '))

    return hours_worked

def get_base_pay():
    """Get the base wage of an employee."""
    base_pay = float(input('Enter the base pay: '))

    return base_pay

def calculate_gross_pay(hours_worked, base_pay):
    """Calculate the gross pay."""
    if hours_worked < 0 or base_pay < 0:
        print("Error! Cannot calculate with negative values.")
    else:
        return hours_worked * base_pay

def calculate_overtime(hours_worked):
    """Calculate overtime pay, provided an employee qualifies for overtime."""
    if hours_worked < 0:
        print("Error! Cannot calculate with negative values.")
    elif hours_worked > MINIMUM_HOURS:
        #Calculate overtime pay.
        overtime_hours = hours_worked - MINIMUM_HOURS
        overtime_pay = overtime_hours * OVERTIME_PAY

        return overtime_pay
    else:
        return 0.0

def deduct_tax(gross_pay):
    """Deduct tax from the gross pay."""
    if gross_pay < 0:
        print("Error! Cannot calculate with negative values.")
    else:
        return gross_pay - (gross_pay * TAX_RATE)

def calculate_net_pay(gross_pay, overtime_pay):
    """Calculate the net pay."""
    if gross_pay < 0 or overtime_pay < 0:
        print("Error! Cannot calculate with negative values.")
    else:
        return gross_pay + overtime_pay

def print_statement(net_pay):
    """Display the net pay."""
    if net_pay < 0:
        print("Error! Unable to comply.")
    else:
        print(f"\nNet pay: ${net_pay:.2f}")