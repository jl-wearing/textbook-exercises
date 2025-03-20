#Program to determine if month * day == year.

#Input
day = int(input('Enter a day of the month: '))
month = int(input('Etner a month of the year: '))
year = int(input('Enter a 2-digit year: '))

#Process
lhs = month * day
if lhs == year:
    print(f"\nThe day {day}/{month}/{year} is magic.")
else:
    print(f"\nThe day {day}/{month}/{year} is not magic.")