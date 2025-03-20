#Program to calculate the pay of an employee including any overtime hours.

#CONSTANTS
OVERTIME_MULTIPLIER = 1.5
BASE_HOURS = 40

#Input
hours_worked = int(input('Enter number of hours worked: '))
wage = float(input('Enter hourly wage: '))

#Process
if hours_worked > BASE_HOURS:
    #Calculate the overtime pay.
    overtime_hours = hours_worked - BASE_HOURS
    overtime_pay = overtime_hours * wage * OVERTIME_MULTIPLIER

    #Calculate the pay without overtime.
    pay = BASE_HOURS * wage

    #Calculate the total wage.
    total_pay = overtime_pay + pay
else:
    total_pay = hours_worked * wage

#Output
print(f"\nPay: ${total_pay:.2f}.")