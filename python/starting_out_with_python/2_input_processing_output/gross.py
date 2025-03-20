#Program to calculate the gross pay of a worker.

#Input
hours_worked = float(input('Enter number of hours worked: '))
hourly = float(input('Enter your hourly wage: '))

#Process
salary = hourly * hours_worked

#Output
print(f"Salary: ${salary:.2f}.\n")