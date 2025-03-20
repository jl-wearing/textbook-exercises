#Program to determine the quarter of the year.

#Input
month = int(input('Enter a month (1-12): '))

#Process
if month >= 1 and month <=3:
    print("\nfirst quarter")
elif month > 3 and month <=6:
    print("\nsecond quarter")
elif month > 6 and month <=9:
    print("\nthird quarter")
elif month > 9 and month <=12:
    print("\nfourth quarter.")
else:
    print("Invalid number entered.")