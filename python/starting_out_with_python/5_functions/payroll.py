#Program to calculate an employee's pay.

#Input
base_pay = float(input('Enter hourly pay rate: '))
hours_worked = float(input('Enter hours worked: '))

#Process
gross_pay = base_pay * hours_worked
MINIMUM_HOURS = 40
OVERTIME_PAY = 10.00

#Calculate overtime pay.
if hours_worked > MINIMUM_HOURS:
    overtime_hours = hours_worked - MINIMUM_HOURS
    overtime_pay = overtime_hours * OVERTIME_PAY

    #add to gross pay
    gross_pay+= overtime_pay

#Deduct tax.
TAX_RATE = 0.14
net_pay = gross_pay - (gross_pay * TAX_RATE)

#Output
print(f"\nWeekly Pay: ${net_pay:.2f}.")